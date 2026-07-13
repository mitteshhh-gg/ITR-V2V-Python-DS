import pandas as pd

ds = pd.read_csv("27-06-std-dataset.csv")

df = pd.DataFrame(ds)

df["Name"] = df["Name"].str.upper()
print(df)