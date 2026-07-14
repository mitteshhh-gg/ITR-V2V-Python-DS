import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Math" : [78,85,80,90,95,76,89,98,78,92],
    "Science" : [92,86,84,74,97,84,87,79,69,81],
    "English" : [74,69,72,59,90,83,85,69,96,89]
})

sns.heatmap(data.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()