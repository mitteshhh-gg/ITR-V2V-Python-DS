#DataFrames
import pandas as pd

data  = {
    "Name": ["Harsh","Mitesh"],
    "Marks": [87,89]
}
print(data)

df = pd.DataFrame(data)
print(df)