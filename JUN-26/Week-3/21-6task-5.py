# Filling The Missing Data
import pandas as pd
import numpy as np
data5 = {
    "Name" : ["Mitesh","Smaran","Harsh","Raj"],
    "Marks" : [84,57,np.nan,90],
}
df5 = pd.DataFrame(data5)
print(f"DATASET : \n{df5}")

fill = df5.fillna(0, inplace=True)                  #Fills missing values with '0'
# fill = df5.fillna(df5["Marks"].mean())              #Fills missing values with 'mean' 
# fill = df5.fillna("Unknown")                      #Fills missing values with 'Unknown'
print(f"After Filling Null Value : \n{fill}")