import pandas as pd

df = pd.read_csv("Datasets/enterprise_survey.csv")

print(df)

print("\nStatistics:\n")

print(df.describe())
