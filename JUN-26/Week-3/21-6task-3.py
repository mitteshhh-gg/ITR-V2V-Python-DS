# Missing Values
import pandas as pd
import numpy as np
data4 = {
    "Name" : ["Mitesh","Smaran","Harsh","Raj"],
    "Marks" : [84,57,np.nan,90],
}

df4 = pd.DataFrame(data4)
print(f"DATASET : \n{df4}")

null = df4.isnull()
print(null)