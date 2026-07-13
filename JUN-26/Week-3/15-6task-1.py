import numpy as np
import matplotlib.pyplot as plt

nums = np.random.randint(1,100,10)
print("Random Numbers : ",nums)

col = ['red', 'green', 'yellow', 'purple', 'orange', 
       'pink', 'brown', 'grey', 'cyan', 'magenta']

bar = plt.bar(range(1,11), nums, color = col)
plt.bar_label(bar)

plt.title("Integer Datasets With Various Colors")
plt.xlabel("DATA POINT")
plt.ylabel("VALUE")
# plt.grid()
plt.show()