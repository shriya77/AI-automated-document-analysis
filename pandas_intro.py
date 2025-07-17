import pandas as pd

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("messy_movies.csv")
print(df)

# Inspect the first few rows of the DataFrame
# print("First five rows of the dataset:")
# print(df.head())

# Get a summary of the DataFrame
# print("\nDataFrame summary:")
# print(df.info())

# print(df.isnull())

df_dropped = df.dropna()
print(df_dropped)

duplicates = df.duplicated()

print("Duplicate rows:\n", duplicates)
