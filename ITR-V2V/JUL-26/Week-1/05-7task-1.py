import seaborn as sns
import matplotlib.pyplot as plt

marks = [45,67,86,83,86,91,84,78,96,86]

sns.boxplot(data = marks)

plt.title("Box-Plot of Marks")
plt.xlabel("Marks")
plt.show()
