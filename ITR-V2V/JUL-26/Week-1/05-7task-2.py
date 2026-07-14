import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.randint(10,100,(10,10))

sns.heatmap(data)
plt.show()