import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df['gender'].value_counts())

print(df.groupby('gender')['math score'].mean())

print(df.groupby('gender')['reading score'].mean())

print(df.groupby('gender')['writing score'].mean())