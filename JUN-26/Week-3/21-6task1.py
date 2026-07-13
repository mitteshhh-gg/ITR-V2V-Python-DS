import pandas as pd

dt = pd.read_excel("employee_data.xlsx")
print(dt)

df = pd.DataFrame(dt)

# print(df[df["Age"] > 50][["First Name","Age"]])
# print(df[df["Salary"] > 45000][["First Name","Salary"]])
# print(df[df["Last Name"] == "Mishra"][["First Name","Last Name","Gender","Salary"]])
# print(df[df["Gender"] == "Female"][["First Name","Last Name"]])
