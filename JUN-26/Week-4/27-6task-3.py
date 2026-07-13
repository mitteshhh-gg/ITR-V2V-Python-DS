import pandas as pd

ds = pd.read_csv("27-06-std-dataset.csv")
df = pd.DataFrame(ds)

df["Date"] = pd.to_datetime(df["Date"])
print(df)