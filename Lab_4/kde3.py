import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
sns.kdeplot(x=df['petal_length'], y=df['petal_width'])

plt.show()