import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

print("---Employee Data Analysis Report---")
emp = pd.read_csv("22-06-emp-dataset.csv")

print(f"DATASET : \n{emp}")
print("--------------------------------------------------")

mp.figure(figsize=(10,5))
bars = mp.bar(emp["Name"], emp["Monthly_Salary"])
mp.title("Salary of Each Employee")
mp.xlabel("Employee Name")
mp.ylabel("Monthly Salary")
mp.bar_label(bars)
mp.show()




