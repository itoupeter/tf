import os
import dicom as dc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PATH = "D:/stage1/patients_info.csv"
df = pd.read_csv(PATH)

plt.hist(df.scans_count, bins = 100)
plt.show()

print(df.describe())
