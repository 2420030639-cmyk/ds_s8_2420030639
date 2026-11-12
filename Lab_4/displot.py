import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.displot(data['total_bill'], kde=False, color='red', bins=20)
plt.show()