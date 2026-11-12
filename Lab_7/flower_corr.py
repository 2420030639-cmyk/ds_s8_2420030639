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

plt.figure(figsize=(8, 6))

sns.heatmap(
    df.iloc[:, :4].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Heatmap of Feature Correlations")

plt.show()
