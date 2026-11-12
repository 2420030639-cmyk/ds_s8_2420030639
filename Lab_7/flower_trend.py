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

plt.plot(df['sepal length (cm)'])

plt.title("Line Chart of Sepal Length")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length")

plt.show()
