import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(200)
y = np.random.randn(200)
sns.kdeplot(x=x, y=y, fill=True)
plt.show()