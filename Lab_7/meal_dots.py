import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(6, 4))

sns.scatterplot(
    x=df['total_bill'],
    y=df['tip'],
    hue=df['sex']
)

plt.title("Scatterplot: Total Bill vs Tip")

plt.show()
