import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("First 5 rows of dataset")
print(df.head())

mean_val = df.mean()
print("\nMean Values:")
print(mean_val)

median_val = df.median()
print("\nMedian Values:")
print(median_val)

mode_val=df.mode()
print("\nMode Values:")
print(mode_val)