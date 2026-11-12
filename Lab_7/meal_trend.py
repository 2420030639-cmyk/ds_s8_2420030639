import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(6, 4))

plt.plot(df['total_bill'])

plt.title("Line Chart of Total Bill")
plt.xlabel("Sample Index")
plt.ylabel("Total Bill")

plt.show()
