# Derma DICOMiser
Python tool to generate test DICOMS that follow the BAD AI Dermatology standard

## Why was this tool built?
This tool was build to allow the generation of DICOM data for use as part of the [MELODY](https://dareuk.org.uk/how-we-work/ongoing-activities/dare-uk-research-exemplars/melody/) project.

## What does this tool do?
The dicomiser takes a metadata CSV and any number of images (JPGs, PNGs etc) and generates a single multi-frame DICOM.

## Prerequisites 
* Python3
* [DCMTK](https://dicom.offis.de/dcmtk.php.en)

## Setup
2. Set an environment variable called `img2dcm` that points to the img2dcm DCMTK tool
    e.g. `$img2dcm=~/jfriel/dmctk/bin/img2dcm`
3. install dependencies ```pip install -r requirements.txt```


## Usage

```
python dicomiser.py OUTPUT_DIRECTORY METADATA_FILE IMAGE...
```

## Metadata file
A template metadata CSV is provided within this repository.
It contains entries for all values that may be populated within the generated DICOM.
All values are optional.

## Limitations
* Multi-Frame images are currently very restricted, and require all images to be the same type and size