import numpy as np
import matplotlib.pyplot as mp

np.random.seed(2)

x = np.random.normal(3,1,100)

y = np.random.normal(150,40,100) / x

trainX = x[:80]     # 80% of the Dataset goes into Training
trainY = y[:80]

testX = x[80:]      # 20% of the Dataset goes into Training
testY = y[80:]

# print(f"R^2 : ")

mp.scatter(trainX, trainY, color = "red", label = "Training Data")
mp.scatter(testX, testY, color = "blue", label = "Testing Data")

mp.xlabel("Minutes Before Purchase")
mp.ylabel("Amount Spent")
mp.legend()
mp.show()
