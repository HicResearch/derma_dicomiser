import sys
import csv
import datetime
from pathlib import Path
import tempfile
import subprocess
import numpy as np
import pydicom
from pydicom.uid import UID, ExplicitVRLittleEndian
import os

def dicomiser():
    output_directory = sys.argv[1]
    metadata = sys.argv[2]
    images = sys.argv[3:]
    metadata_dict = csvToDict(metadata)
    dcm = imagesToDICOM(images)
    dcm = populateDICOM(metadata_dict,dcm)
    saveDICOM(dcm,output_directory,images[0])

def populateDICOM(metadata_dict,ds):
    ds.PatientName = metadata_dict.get('PatientName',None)
    ds.PatientID = metadata_dict.get('PatientID',None)
    ds.PatientSex = metadata_dict.get('PatientSex',None)
    ds.StudyDate = datetime.datetime.strptime(metadata_dict.get('StudyDate',None), '%d/%m/%Y')
    ds.StudyTime = metadata_dict.get('StudyTime',None)
    ds.PatientBirthDate = datetime.datetime.strptime(metadata_dict.get('PatientBirthDate',None), '%d/%m/%Y').date()
    dt = datetime.datetime.now()
    ds.ContentDate = dt.strftime("%Y%m%d")
    ds.ContentTime = dt.strftime("%H%M%S.%f")  # long format with micro seconds
    ds.Modality = "DMS"
    return ds

def imagesToDICOM(images):
    files = []
    for image in images:
         path = Path(tempfile.NamedTemporaryFile(suffix=".dcm").name)
         subprocess.run([os.environ['img2dcm'],image,path])
         files.append(path)
        
    datasets = [pydicom.dcmread(f) for f in files]

    for d in datasets:
        if d.file_meta.TransferSyntaxUID.is_compressed:
            d.decompress()

    ds = datasets[0]

    pixel_arrays = np.stack([d.pixel_array for d in datasets])
   

    pixel_arrays = np.stack(pixel_arrays)

    ds.PixelData = pixel_arrays.tobytes()

    ds.NumberOfFrames = len(datasets)
    ds.Rows = datasets[0].Rows
    ds.Columns = datasets[0].Columns
    ds.SOPInstanceUID = pydicom.uid.generate_uid() 

    ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    ds.is_little_endian = True
    ds.is_implicit_VR = False

    if hasattr(ds, "InstanceNumber"):
        del ds.InstanceNumber
    for file in files:
        os.remove(file)
    return ds



def saveDICOM(dcm,output_directory,image_path):
    path = os.path.join(output_directory,Path(image_path).name.split('.')[0]+'.dcm')
    print(f"Writing dataset to: {path}")
    dcm.save_as(path, enforce_file_format=True)

def csvToDict(metadataCSV):
    with open(metadataCSV, mode='r') as infile:
        reader = csv.DictReader(infile)
        return next(reader)

if __name__ == "__main__":
    dicomiser()