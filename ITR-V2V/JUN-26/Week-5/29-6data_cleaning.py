import pandas as pd

print("----- DATA CLEANING REPORT -----")

df = pd.read_csv("employee_dataset.csv")

print(df.head())
print(df.info())
print(df.describe())
print("Shape:", df.shape)

original_rows = len(df)

# Missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Monthly_Salary"] = df["Monthly_Salary"].fillna(df["Monthly_Salary"].median())
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# Duplicates
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

# Outliers (IQR on Monthly_Salary)
Q1 = df["Monthly_Salary"].quantile(0.25)
Q3 = df["Monthly_Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

before = len(df)
df = df[(df["Monthly_Salary"] >= lower) & (df["Monthly_Salary"] <= upper)]
outliers = before - len(df)

# Feature Engineering
df["Salary_Category"] = df["Monthly_Salary"].apply(lambda x: "High" if x>=60000 else "Medium" if x>=40000 else "Low")

# Merge another dataset
dept = pd.DataFrame({
    "Department":["IT","HR","Sales","Finance"],
    "Location":["Pune","Mumbai","Delhi","Bengaluru"]
})

df = pd.merge(df, dept, on="Department", how="left")

df.to_csv("employee_dataset_cleaned.csv", index=False)

print("\nOriginal Rows =", original_rows)
print("Duplicate Rows Removed =", duplicates)
print("Outliers Removed =", outliers)
print("Final Rows =", len(df))
print("Dataset Successfully Cleaned!")
