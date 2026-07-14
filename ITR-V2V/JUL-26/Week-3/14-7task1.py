from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt 

stdHr = np.array([5,3,7,8,2,4,
                  6,9,1,10,0,1]).reshape(-1,1)

marks = np.array([59,25,68,72,28,49,
                  57,96,26,98,9,19])

lin = LinearRegression().fit(stdHr, marks)

score = lin.score(stdHr, marks)
print("Score of the Model : ", score)

marksPred = lin.predict(stdHr)

plt.scatter(stdHr, marks, color = "blue", label = "Actual Marks")
plt.plot(stdHr, marksPred, color = "red", label = "Predicted Marks")

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.title("Linear Regression: Study Hours vs Marks")
plt.legend()
plt.show()
