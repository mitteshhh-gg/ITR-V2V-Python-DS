import pandas as pd

print("----- DATA CLEANING REPORT -----")

emp = pd.read_csv("29-06-Employee.csv")

print(f"DATASET : \n{emp}")
print("............................................................................")

print(f"Top 10 Entries : \n{emp.head(10)}")
print("............................................................................")

print(f"{emp.info()}")
print("............................................................................")

print(f"Summary of Table : \n{emp.describe()}")
print("............................................................................")

print(f"Shape of Dataset : {emp.shape}")
print("............................................................................")

rows = len(emp)

# Removing Missing values 
miss = emp.isnull().sum()
emp = emp.dropna()

# Removing Duplicates
dup = emp.duplicated().sum()
emp = emp.drop_duplicates()

emp.sort_values("Age")

# Outliers
Q1 = emp["Monthly_Salary"].quantile(0.25)
Q3 = emp["Monthly_Salary"].quantile(0.75)
IQR = Q3 - Q1

outliers = emp[
    (emp["Monthly_Salary"] < (Q1 - 1.5 * IQR)) |
    (emp["Monthly_Salary"] > (Q3 + 1.5 * IQR))
]

print(f"Outliers  : \n{outliers}")
print("............................................................................")

# Feature Engineering : Creating new column "Bonus" where salary increments by 10%
emp["Bonus"] = emp["Monthly_Salary"] * 0.10

# Merge another dataset
dept = pd.DataFrame({
    "Department":["IT","HR","Sales","Finance"],
    "Location":["Pune","Mumbai","Delhi","Bengaluru"]
})

emp = pd.merge(emp, dept, on="Department", how="left")
emp.to_csv("29-06-EmpCleanedDS.csv")

# Bonus Feature : Exporting into Excel 
emp.to_excel("29-06-EmpCleanedDS.xlsx")
print("Excel File Saved Successfully!")

# Displaying all data 
print("............................................................................")
print(f"\nOriginal Rows : {rows}")
print(f"Missing Rows Removed : \n{miss}")
print(f"Duplicate Rows Removed : {dup}")
print(f"Final Rows : {len(emp)}")
print("Dataset Successfully Cleaned!")


