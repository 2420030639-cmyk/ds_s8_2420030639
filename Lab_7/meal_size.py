import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(6, 4))

plt.scatter(
    df['total_bill'],
    df['tip'],
    s=df['size'] * 20,
    alpha=0.5,
    c=df['size']
)

plt.title("Bubble Chart: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()
