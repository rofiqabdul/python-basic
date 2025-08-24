import pandas as pd

filepath = 'Titanic.csv'

df = pd.read_csv(filepath)
print(df.head())

missing_before = df['Age'].isnull().sum()
print(f"Number of missing 'Age' values before filling: {missing_before}")

median_age = df['Age'].median()
print(f"The median age of the dataset is: {median_age:.2f}")

number_of_survivors = df['Survived'].sum()
total_passengers = len(df)
survival_rate = (number_of_survivors / total_passengers) * 100

print(f"Total passengers: {total_passengers}")
print(f"Number of survivors: {number_of_survivors}")
print(f"Overall survival rate: {survival_rate:.2f}%")

median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

survival_rate_by_gender = df.groupby('Sex')['Survived'].mean() * 100