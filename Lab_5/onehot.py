import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
})

one_hot = pd.get_dummies(df, columns=['Color'])
print(one_hot)