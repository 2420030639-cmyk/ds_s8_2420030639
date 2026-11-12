import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

df = pd.DataFrame(tips)
                    
print("First 5 rows of dataset")
print(df.head())

skewness_val = df.skew(numeric_only=True)

print("\nSkewness Values:")
print(skewness_val)

kurtosis_val = df.kurtosis(numeric_only=True)

print("\nKurtosis Values:")
print(kurtosis_val)