# Group-By Operation
import pandas as pd
import numpy as np
data6 = {
    "Dept" : ["HR","IF","HR","IF"],
    "Salary" : [75000,55000,49000,51000]
}

df6 = pd.DataFrame(data6)
print(f"DATASET : \n{df6}")

grp = df6.groupby("Dept")["Salary"].mean()
print(f"After Grouping : \n{grp}")

# grp = df6.groupby("Dept")["Salary"].sum()
# print(f"After Grouping : \n{grp}")