import pandas as pd 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
df = pd.read_csv("18-7data.csv")

X = df[["Volume","Weight"]]

scaledX = sc.fit_transform(X)

print(scaledX)