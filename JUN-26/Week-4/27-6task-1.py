import pandas as pd
import numpy as np

df = pd.read_csv("student_dataset.csv")

nval = df.isnull()                      #finding missing values
print(f"Missing Values in DATASET : \n{nval}")

df["Age"] = df["Age"].fillna(int(df["Age"].mean()))

df["Marks"] = df["Marks"].fillna(0)                 

df["City"] = df["City"].fillna("Unknown")
print(f"After Filling Missing Values : \n{df}")

print(f"Duplicate Values :\n{df.duplicated()}")      #finding duplicated
 
df = df.sort_values("Student_ID")      #Sorting
print(f"After Sorting : \n{df}")

df.to_csv("cleanedStdDS.csv")









# df["Age"] = df["Age"].fillna(df["Age"].mean())
# sorting.to_csv("cleanedStdDS.csv", index=False)
# df.to_csv("cleanedStdDS.csv")