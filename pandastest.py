import pandas as pd

PATH = r"C:\Users\itoup\Documents\GitHub\tf\lungcancer\stage1_sample_submission.csv\stage1_sample_submission.csv"
df = pd.read_csv(PATH)

print(df)

PATH = r"C:\Users\itoup\Documents\GitHub\tf\lungcancer\stage1_labels.csv\stage1_labels.csv"
df = pd.read_csv(PATH)

print(df)
