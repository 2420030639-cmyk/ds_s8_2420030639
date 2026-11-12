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

plt.figure(figsize=(6, 4))

sns.barplot(
    x=df['species'],
    y=df['sepal length (cm)']
)

plt.title("Bar Chart: Mean Sepal Length by Species")

plt.xticks(
    [0, 1, 2],
    iris.target_names
)

plt.show()
