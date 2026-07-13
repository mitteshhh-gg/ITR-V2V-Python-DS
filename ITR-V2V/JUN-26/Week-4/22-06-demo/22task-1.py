import pandas as pd
import numpy as np

print("---Employee Data Analysis Report---")
emp = pd.read_csv("employee_salary_dataset.csv")

print(f"DATASET : \n{emp}")
print("--------------------------------------------------")
print((f"Average salary : {np.mean(emp["Monthly_Salary"])}rs"))
print(f"Highest Salary : {np.max(emp["Monthly_Salary"])}rs")
print(f"Lowest Salary : {np.min(emp["Monthly_Salary"])}rs")

dept = pd.DataFrame(emp)
deptAvgSal = dept.groupby("Department")["Monthly_Salary"].mean()
print("--------------------------------------------------")
print(f"---Department-Vise Average Salaries---\n{deptAvgSal}")

print("--------------------------------------------------")
print("---Handling Missing Values---")

nvalue1 = dept[["Name","Department","Gender","City"]].fillna("Unknown")

nvalue2 = dept[["Monthly_Salary","Age"]].fillna(0)
print(f"Missing Values : \n{nvalue1}\n{nvalue2}") 

print(dept.sort_values("Monthly_Salary"))
































# print(f"Missing Names : \n{nvalue1}")
# dept = dept.fillna({
#     "Name": "Unknown",
#     "Department": "Unknown",
#     "Gender": "Unknown",
#     "City": "Unknown",
#     "Age": 0,
#     "Monthly_Salary": 0
# })