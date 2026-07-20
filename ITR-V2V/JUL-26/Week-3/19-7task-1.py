import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("19-7comedy_show.csv")

d = {"UK" : 0 , "USA" : 1, "N" : 2}
df["Nationality"] = df["Nationality"].map(d)

d = {"YES" : 1, "NO" : 0}
df["Go"] = df["Go"].map(d)

features = ["Age", "Experience", "Rank", "Nationality"]

X = df[features]
y = df["Go"]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)
plt.show()

# Should I see a 40yr old - american comdeian - 10yr experience - Comedy Ranking 7
print(dtree.predict([[40,10,7,1]]))
