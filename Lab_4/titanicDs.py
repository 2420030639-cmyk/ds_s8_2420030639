import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

print(df.head(6))

objective = "Classification: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalanced classes"

print("Objective:", objective)
print("Success Criteria:", success_criteria)
print("Constraints:", constraints)

print("Data shape:", df.shape)
print(df.info())
print(df.describe())

# Handle missing values
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert categorical columns into numerical values
df = pd.get_dummies(
    df,
    columns=['sex', 'class', 'embarked'],
    drop_first=True
)

# Create family size feature
df['family_size'] = df['sibsp'] + df['parch']

print(df.head(6))