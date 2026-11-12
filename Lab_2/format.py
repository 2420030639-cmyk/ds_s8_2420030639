import pandas as pd

df = pd.DataFrame ({
    'Date': ['2025-01-05', '05/01/2025', 'Jan 5, 2025', '2025.01.05']
})
print(df)
print("\n")

df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
print(df)