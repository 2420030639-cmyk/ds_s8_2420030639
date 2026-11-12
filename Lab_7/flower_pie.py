import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df['species'] = iris.target

species_counts = df['species'].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    species_counts,
    labels=iris.target_names,
    autopct='%1.1f%%'
)

plt.title("Species Distribution")

plt.show()
