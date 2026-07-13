import pandas as pd

emp = pd.read_csv("28-06-EmpDataset/28-06-empSalaryDS-2.csv")
print(emp)

print(f"SORTED : \n{emp.sort_values("Monthly_Salary")}")
Q1 = emp["Monthly_Salary"].quantile(0.25)
Q3 = emp["Monthly_Salary"].quantile(0.75)

IQR = Q3 - Q1
print(f"IQR : {IQR}")

outliers = emp[(emp["Monthly_Salary"] < (Q1 - 1.5 * IQR)) | 
                (emp["Monthly_Salary"] > (Q3 + 1.5 * IQR))]
print(f"Outliers : {outliers}")