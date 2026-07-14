import numpy as np
import matplotlib.pyplot as mp
from sklearn.linear_model import LinearRegression 

X = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

model = LinearRegression().fit(X,y)

print(f"Intercept : {model.intercept_}")
print(f"Slope : {model.coef_}")
print(f"R^2 Score : {model.score(X,y)}")

yPred = model.predict(X)
print(f"Prediction : {yPred}")

mp.figure(figsize=(8,5))
mp.scatter(X, y, color = "red", label = "Data Point")
mp.plot(X, yPred, color = "pink", linewidth = 3, label = "Regression Line")
mp.xlabel("X values")
mp.ylabel("Y values")
mp.title("Linear Regression")
mp.legend()
mp.grid(True)
mp.show()
