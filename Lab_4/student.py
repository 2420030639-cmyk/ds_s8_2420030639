import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].mean())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].mean())

df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])

df.drop_duplicates(inplace=True)

df = pd.get_dummies(df, columns=['Gender', 'Department', 'City'], drop_first=True)

print(df.head())
print(df.shape)

'''sns.histplot(df['Attendance'], bins=20, kde=True)
plt.title("Attendance Distribution")
plt.show()'''

corr = df[['Age', 'Attendance', 'Math_Score', 'Science_Score']].corr()
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Student Correlation Matrix")
plt.show()