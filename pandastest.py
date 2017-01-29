import os
import dicom as dc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FOLDER = "D:/stage1/stage1"
OUTPUT_FOLDER = "D:/stage1"
patients = os.listdir(INPUT_FOLDER)
patients.sort()

scans_counts = []

for patient in patients:
    PATIENT_FOLDER = INPUT_FOLDER + '/' + patient
    scans = os.listdir(PATIENT_FOLDER)
    scans_counts.append(len(scans))

df = pd.DataFrame({"id": patients, "scans_count": scans_counts})
df.to_csv(OUTPUT_FOLDER + "/patients_info.csv")

print(df)
