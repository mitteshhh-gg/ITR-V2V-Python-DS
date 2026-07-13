import numpy as np
import matplotlib.pyplot as plt

quantity = np.array([120,150,100,80,130])

print("Total Sales = ", np.sum(quantity))
print("Average Sales = ", np.average(quantity))
print("Lowest Sales = ", np.min(quantity))
print("Highest Sales = ", np.max(quantity))

brand = ["IPhone","Vivo","Oppo","Lava","IQOO"]

plt.bar(brand,quantity)
plt.title("Mobile Sales Analysis")
plt.xlabel("Mobile Brands")
plt.ylabel("Quantity")
plt.show()