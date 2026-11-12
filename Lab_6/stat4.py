import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

df = pd.DataFrame(tips)

print("First 5 rows of dataset")
print(df.head())

# Range
range_val = df.max(numeric_only=True) - df.min(numeric_only=True)

print("\nRange Values:")
print(range_val)

# Variance
variance_val = df.var(numeric_only=True)

print("\nVariance Values:")
print(variance_val)

# Standard Deviation
std_val = df.std(numeric_only=True)

print("\nStandard Deviation Values:")
print(std_val)

# Quartiles
Q1 = df.quantile(0.25, numeric_only=True)

Q3 = df.quantile(0.75, numeric_only=True)

# Interquartile Range
IQR = Q3 - Q1

print("\nInterquartile Range (IQR) Values:")
print(IQR)