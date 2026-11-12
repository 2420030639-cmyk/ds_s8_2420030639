import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.countplot(x='sex', hue = 'smoker', data=data)
plt.show()