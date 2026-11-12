import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import seaborn as sns

tips = sns.load_dataset('tips')
print("Original DataFrame:")
print(tips.head())

#Min-Max Normalization
numeric_cols = tips.select_dtypes(include=['float64', 'int64']).columns
scaler_minmax = MinMaxScaler()
tips_normalized = tips.copy()
tips_normalized[numeric_cols] = scaler_minmax.fit_transform(tips[numeric_cols])
print("\nNormalized DataFrame:")
print(tips_normalized.head())

#Scaling using StandardScaler
scaler_standard = StandardScaler()
tips_standardized = tips.copy()
tips_standardized[numeric_cols] = scaler_standard.fit_transform(tips[numeric_cols])
print("\nStandardized DataFrame:")
print(tips_standardized.head())

#Encoding categorical variables using LabelEncoder
#(a) One-Hot Encoding
tips_one_hot = pd.get_dummies(tips, columns=['sex', 'smoker', 'day', 'time'])
print("\nOne-Hot Encoded DataFrame:")