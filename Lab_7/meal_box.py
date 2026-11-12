import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(6, 4))

sns.boxplot(
    x=df['total_bill']
)

plt.title("Box Plot of Total Bill")

plt.show()
