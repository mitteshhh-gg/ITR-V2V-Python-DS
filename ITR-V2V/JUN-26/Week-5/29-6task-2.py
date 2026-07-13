import pandas as pd

emp = pd.read_csv("29-Employee.csv")
print(f"DATASET : \n{emp}")

print("------------------------------------------------------------")

print(f"Top 10 Entries : \n{emp.head(10)}")
print("------------------------------------------------------------")

print(f"Info about : \n{emp.info()}")
print("------------------------------------------------------------")

print(f"Summary of Table : \n{emp.describe()}")
print("------------------------------------------------------------")

print(f"Shape of Dataset : {emp.shape}")
print("------------------------------------------------------------")

print(f"Missing Values Removed : \n{emp.isnull().dropna().sum()}")
print("------------------------------------------------------------")

print(f"Duplicate records removed:{emp.duplicated().dropna().sum()}")
print("------------------------------------------------------------")

emp.sort_values("Age")
Q1 = emp["Age"].quantile(0.25)
Q3 = emp["Age"].quantile(0.75)

IQR = Q3-Q1
print(f"IQR : {IQR}")

outliers = emp[
    (emp["Age"] < (Q1-1.5*IQR)) |
    (emp["Age"] > (Q3+1.5*IQR))
]

print("Outliers:\n",outliers.drop("Age").sum())
