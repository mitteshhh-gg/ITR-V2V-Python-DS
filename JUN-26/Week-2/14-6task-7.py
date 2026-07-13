import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,100,10)
print(data)

bar = plt.bar(range(1,11),data,color = 'red')

plt.bar_label(bar)
plt.title("RANDOM INTEGER DATASET")
plt.xlabel("DATA POINT")
plt.ylabel("VALUE")
plt.grid()
plt.show()