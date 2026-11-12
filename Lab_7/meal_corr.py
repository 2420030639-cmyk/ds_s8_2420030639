import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(8, 6))

sns.heatmap(
    df[['total_bill', 'tip', 'size']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Heatmap of Tips Dataset Correlations")

plt.show()
