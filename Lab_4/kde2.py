import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
sns.kdeplot(x=df['petal_length'])
sns.kdeplot(x=df['petal_width'], shade=True)

plt.show()