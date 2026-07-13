import pandas as pd
data3 = {
    "Name" : ["Mitesh","Smaran","Harsh","Raj"],
    "Marks" : [84,57,45,90],
    "Age" : [20,22,25,27]
}

df3 = pd.DataFrame(data3)

print(df3[df3["Marks"] > 40] [["Name","Marks"]])
# print(df3[["Name","Marks"]])