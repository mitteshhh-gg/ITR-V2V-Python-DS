'''
predict the CO2 emission of a car where the weight is 2300kg,
and volume is 1300cm^3
'''

import pandas as pd
import matplotlib.pyplot as mp
from sklearn.linear_model import LinearRegression as lr
import numpy as np


df = pd.read_csv("18-7data.csv")

X = df[["Volume", "Weight"]]
y = df["CO2"]

regr = lr().fit(X, y)

arr = np.array([[1300, 2300]])
prediction1 = regr.predict(arr)
print(f"Prediction : {prediction1[0]}")











# print(f"R^2 : {regr.score(X,y)}")
mp.scatter(df["Volume"], y, color="blue", label = "Volume")
mp.scatter(df["Weight"], y, color="red", label = "Weight")

mp.plot(arr[0][1], prediction1, color = "black", marker = "*", markersize = 10, label = "Regression Line")
# mp.plot(arr[0][1], prediction1, color="green", label = "Regression Line")

mp.xlabel("Volume - Weight")
mp.ylabel("CO2")
mp.legend()
mp.show()
