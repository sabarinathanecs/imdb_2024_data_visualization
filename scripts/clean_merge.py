import pandas as pd
import os

df = pd.read_csv("../data/imdb_2024_movies.csv")
df["Genre"] = df["Genre"].str.strip()

if not os.path.exists("../data"):
    os.makedirs("../data")

genres = df["Genre"].unique()

for genre in genres:
    genre_df = df[df["Genre"] == genre]
    genre_df.to_csv(f"../data/{genre}.csv", index=False)

print("Genre-wise CSV files created.")

