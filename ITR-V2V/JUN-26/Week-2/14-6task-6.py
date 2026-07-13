import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,100,10)
print(data)

plt.plot(range(1,11),data,color = "pink")
plt.title("RANDOM INTEGER DATASET")
plt.xlabel("DATA POINT")
plt.ylabel("VALUE")
plt.show()