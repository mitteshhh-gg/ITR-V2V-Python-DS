import numpy as np
import matplotlib.pyplot as plt

sales = np.array([25000,38000,24000,56000,40000])

print("Mean Sales = ", np.mean(sales))
print("Median Sales = ", np.median(sales))
print("Standard Deviation = ", np.std(sales))

months = ["Jan","Feb","Mar","Apr","May"]

plt.bar(months,sales)
plt.title("Monthly Sales Analysis")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
