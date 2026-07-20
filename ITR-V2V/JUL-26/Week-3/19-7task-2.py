import numpy as np
import matplotlib.pyplot as mp
from sklearn.metrics import r2_score

np.random.seed(2)
X = np.random.normal(3,1,100)
y = np.random.normal(150,40,100) / X

trainX = X[:80]     # 80% of the Dataset goes into Training
trainY = y[:80]

testX = X[80:]      # 20% of the Dataset goes into Training
testY = y[80:]

model = np.poly1d(np.polyfit(trainX, trainY,4))
r2 = r2_score(testY, model(testX))

print(f"R^2 : {r2} ")
print(f"How much money will a customer spend after shopping for 5 minutes : {model(5)}")

mp.scatter(trainX, trainY, color = "red", label = "Training Data")
mp.scatter(testX, testY, color = "blue", label = "Testing Data")

mp.plot(testX, model(testX), color = "green", label = "Polynomial Fit")

mp.xlabel("Minutes Before Purchase")
mp.ylabel("Amount Spent")

mp.legend()
mp.show()

