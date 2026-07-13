# Sorting : 
import pandas as pd
data2 = {
    "Name" : ["Mitesh","Smaran","Harsh","Raj"],
    "Marks" : [84,57,45,90]
}

# df2 = pd.DataFrame(data2)
# print(df2)
# print(df2[df2["Marks"] > 60])

df2 = pd.DataFrame(data2)
asc = df2.sort_values("Marks")            #Ascending Order By-Default
print(f"Ascending : \n{asc}")

des = df2.sort_values("Marks", ascending= False)      #Descending Order
print(f"Descending : \n{des}")