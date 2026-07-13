# Filtering : 
import pandas as pd
data1 = {
    "Name" : ["Mitesh","Smaran","Harsh","Raj"],
    "Marks" : [84,57,45,90]
}
df1 = pd.DataFrame(data1)
print(f"DATASET : \n{df1}")
 
fil = df1[df1["Marks"] > 60]
print(f"After Filtering : \n{fil}")





# print("\n")
# print(df1["Marks"] > 60)