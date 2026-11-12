import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')
sns.boxplot(data['total_bill'])