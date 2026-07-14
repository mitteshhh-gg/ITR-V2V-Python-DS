import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as mp

# X represents the size of tumor in cm
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 
              4.92, 4.37, 4.96, 4.52, 3.69, 5.88 ]).reshape((-1,1))

# Y represents whether the tumour is cancerous or not
y = np.array([0, 0, 0, 0, 0, 0,
              1, 1, 1, 1, 1, 1])

logr = LogisticRegression().fit(X,y)

# Prdeict if tumor is cancerous 
predicted1 = logr.predict(X)
predicted2 = logr.predict(np.array([6.17,4.2,0.6]).reshape((-1,1)))
print(predicted1)
print(predicted2)






















# col = ["red" if pred == 1 else "green" for pred in predicted]
# mp.scatter(X, predicted, color = col, label = "Cancerous")
# mp.legend()
# mp.show()