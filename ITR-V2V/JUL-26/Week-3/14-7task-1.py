# Suprise-Test Question
import pandas as pd
import numpy as np

df = pd.read_csv("14-7imdb_movies.csv")
df = pd.DataFrame(df)

print("---IMDB Movies Dataset Summary---")
print("Number of Rows :", len(df))
print("Number of Columns :", len(df.columns))
print(f"Summary : \n{df.describe()}")
print("\n---------------------------------------------\n")
print("Title of First 10 Movies in the Dataset : ")
print(df["Series_Title"].head(10))

print("Cleaning Dataset : ")
miss = df.isnull().sum().sum()  # Count Missing Values
df = df.dropna()                # Drop Missing Values

dup = df.duplicated().sum()     # Count Duplicate Values
df = df.drop_duplicates()       # Drop Duplicates

df = df.sort_values("Released_Year")
df = df.reset_index()

print(f"Removed Missing Values : {miss}")
print(f"Removed Duplicate Values : {dup} ")
print("Dataset Cleaned Successfully!")

df = df.to_csv("14-7imdb_movies_cleaned.csv")
cdf = pd.read_csv("14-7imdb_movies_cleaned.csv")
print(cdf)
