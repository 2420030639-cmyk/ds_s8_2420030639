import pandas as pd

import seaborn as sns

tips = sns.load_dataset("tips")

df = pd.DataFrame(tips)

print("First 5 rows of dataset")
print(df.head())

mean_val = df.mean(numeric_only=True)

print("\nMean Values:")
print(mean_val)

median_val = df.median(numeric_only=True)

print("\nMedian Values:")
print(median_val)

mode_val = df.mode()

print("\nMode Values:")
print(mode_val)