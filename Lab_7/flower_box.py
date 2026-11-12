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

sns.boxplot(x=df['sepal length (cm)'])

plt.title("Box Plot")

plt.show()
