import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(6, 4))

sns.violinplot(
    x=df["day"],
    y=df["total_bill"]
)

plt.title("Violin Plot: Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()
