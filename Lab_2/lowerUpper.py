import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'BOB', 'charlie', 'DAVID']
})
print(df)
print("\n")

df['Name_lower'] = df['Name'].str.lower()
df['Name_upper'] = df['Name'].str.upper()
print(df)