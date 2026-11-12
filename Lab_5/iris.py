import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import seaborn as sns

import tips

iris = sns.load_dataset('iris')
print("Original DataFrame:")
print(iris.head())

numeric_cols = iris.select_dtypes(include=['float64', 'int64']).columns
scaler_minmax = MinMaxScaler()
iris_normalized = iris.copy()
iris_normalized[numeric_cols] = scaler_minmax.fit_transform(iris[numeric_cols])
print("\nNormalized DataFrame:")
print(iris_normalized.head())

scaler_standard = StandardScaler()
iris_standardized = iris.copy()
iris_standardized[numeric_cols] = scaler_standard.fit_transform(iris[numeric_cols])
print("\nStandardized DataFrame:")
print(iris_standardized.head())

iris_one_hot = pd.get_dummies(iris, columns=['species'])
print("\nOne-Hot Encoded DataFrame:")