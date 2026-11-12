import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

day_counts = df['day'].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    day_counts,
    labels=day_counts.index,
    autopct='%1.1f%%'
)

plt.title("Distribution of Customers by Day")

plt.show()
