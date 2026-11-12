import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(6, 4))

sns.barplot(
    x=df['day'],
    y=df['total_bill']
)

plt.title("Bar Chart: Mean Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Mean Total Bill")

plt.show()
