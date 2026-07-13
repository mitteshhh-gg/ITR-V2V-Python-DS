import pandas as pd
import numpy as np

ds = pd.read_csv("student_dataset.csv")
print(f"DATASET : \n{ds}") 

df = pd.DataFrame(ds)

nval = df.isnull()
print(f"Missing Values in DATASET : \n{nval}")

fillval1 = df.fillna(df["Age"].mean())
print(f"After Filling Age : \n{fillval1}")

fillval2 = df["Marks"].fillna(0)
print(f"After Filling Marks : \n{fillval2}")

fillval3 = df["City"].fillna("Unknown")
print(f"After Filling City : \n{fillval3}")

sorting = df.sort_values("Student_ID")
print(f"After Sorting : \n{sorting}")


nval.to_csv("cleanedStdDS.csv")
fillval1.to_csv("cleanedStdDS.csv")
fillval2.to_csv("cleanedStdDS.csv")
fillval3.to_csv("cleanedStdDS.csv")
sorting.to_csv("cleanedStdDS.csv")

# df.to_csv("cleanedStdDS.csv")

# dup = df["City"].duplicated()
# print(f"Duplicated Value : \n{dup}")

# df.to_csv("cleaned_student_DS.csv",index=False)