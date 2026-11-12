import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")

c_p={'Male': 'lightblue', 'Female': 'pink'}
sns.pairplot(data, hue="sex", palette=c_p)
plt.show()