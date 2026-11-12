import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=data, kind="hex", color="k")
plt.show()