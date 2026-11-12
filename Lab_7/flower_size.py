import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df['species'] = iris.target

plt.figure(figsize=(6, 4))

plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    s=df['petal length (cm)'] * 20,
    alpha=0.5,
    c=df['species']
)

plt.title("Bubble Chart: Sepal vs Petal")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

plt.show()
