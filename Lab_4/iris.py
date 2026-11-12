import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')
sns.pairplot(data, hue='species')
plt.show()