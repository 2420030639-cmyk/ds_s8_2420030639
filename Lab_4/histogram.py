import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

sns.histplot(df['age'], bins=10, kde=True)
plt.title("Age Distribution")
plt.show()

df = sns.load_dataset("tips")

sns.histplot(df['size'], bins=20, kde=True)
plt.title("Size Distribution")
plt.show()