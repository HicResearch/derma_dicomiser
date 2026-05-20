
from randomtimestamp import randomtimestamp
import random
from faker import Faker
import csv
def generateTestData():
    fake = Faker()

    StudyDate = randomtimestamp(text=False).strftime("%d/%m/%Y")
    StudyTime = randomtimestamp(text=False).strftime("%H%M%S")
    AccessionNumber =random.randint(1,10000)
    PatientID = random.randint(1,10000)
    PatientName = fake.name()
    PatientBirthDate =randomtimestamp(text=False).strftime("%d/%m/%Y")
    PatientSex = random.choice(['M','F','O'])
    EthnicGroup = random.choice([
        'WHITEBRITISH',
        'WHITEIRISH',
        'WHITEOTHER',
        'MIXEDCARIBBEAN',
        'MIXEDAFRICAN',
        'MIXEDWHITEASIAN',
        'MIXEDOTHER',
        'ASIANINDIAN',
        'ASIANPAKISTANI',
        'ASIANBANGLADESHI',
        'ASIANOTHER',
        'BLACKCARRIBBEAN',
        'BLACKAFRICAN',
        'BLACKOTHER',
        'OTHERCHINESE',
        'OTHERANY',
        'CHINESE'
    ])
    FitzpatrickSkinType = random.choice([
        'C74569',
        'C74570',
        'C74571',
        'C74572',
        'C74573'
    ])
    PreviousHistoryOfSkinMalignantMelanoma = random.choice(['321000119108',None])
    PreviousHistoryOfSkinMalignantMelanomaTotalNoCases= random.choice([0,1,2,3])
    FamilyHistoryOfSkinMalignantMelanoma = random.choice(['Y','N'])
    FamilyHistoryOfSkinMalignantMelanomaTotalNoCases=random.choice([0,1,2,3])
    PreviousHistoryOfSkinNonMalignantMelanoma =random.choice(['428053000',None])
    PreviousHistoryOfSkinNonMalignantMelanomaTotalNoCases=random.choice([0,1,2,3])
    AnatomicalLocation = random.choice([
        69536005,
        85562004,
        123851003,
        416775004,
        53120007,
        61685007
    ])
    Laterality = random.choice([
        'R',
        'L',
        'B',
        'U'
    ])
    InstitutionName = 'Some Hospital'
    SymptomOfLesion=random.choice([None,'Itching','Redness','Bleeding','Pain','Other'])
    ChangeToLesionSize=random.choice(['Y','N'])
    ChangeToLesionShape=random.choice(['Y','N'])
    ChangeToLesionColour=random.choice(['Y','N'])
    LesionPalpationFindings=random.choice([130485,130486,None])
    PreviousSkinProcedures=random.choice([240977001,302396003,428604001,None])
    DiagnosisStage=random.choice(['Triage','Consultation','Biopsy','Final'])
    FinalDiagnosis=random.choice(['2C30','2F3Y'])

    print("StudyDate,StudyTime,AccessionNumber,PatientID,PatientName,PatientBirthDate,PatientSex,EthnicGroup,FitzpatrickSkinType,PreviousHistoryOfSkinMalignantMelanoma,PreviousHistoryOfSkinMalignantMelanomaTotalNoCases,FamilyHistoryOfSkinMalignantMelanoma,FamilyHistoryOfSkinMalignantMelanomaTotalNoCases,PreviousHistoryOfSkinNonMalignantMelanoma,PreviousHistoryOfSkinNonMalignantMelanomaTotalNoCases,AnatomicalLocation,Laterality,InstitutionName,SymptomOfLesion,ChangeToLesionSize,ChangeToLesionShape,ChangeToLesionColour,LesionPalpationFindings,PreviousSkinProcedures,DiagnosisStage,FinalDiagnosis")
    print(
        ','.join((str(StudyDate),
        str(StudyTime),
        str(AccessionNumber),
        str(PatientID),
        str(PatientName),
        str(PatientBirthDate),
        str(PatientSex),
        str(EthnicGroup),
        str(FitzpatrickSkinType),
        str(PreviousHistoryOfSkinMalignantMelanoma),
        str(PreviousHistoryOfSkinMalignantMelanomaTotalNoCases),
        str(FamilyHistoryOfSkinMalignantMelanoma),
        str(FamilyHistoryOfSkinMalignantMelanomaTotalNoCases),
        str(PreviousHistoryOfSkinNonMalignantMelanoma),
        str(PreviousHistoryOfSkinNonMalignantMelanomaTotalNoCases),
        str(AnatomicalLocation),
        str(Laterality),
        str(InstitutionName),
        str(SymptomOfLesion),
        str(ChangeToLesionSize),
        str(ChangeToLesionShape),
        str(ChangeToLesionColour),
        str(LesionPalpationFindings),
        str(PreviousSkinProcedures),
        str(DiagnosisStage),
        str(FinalDiagnosis)))
    )

if __name__ == "__main__":
    generateTestData()