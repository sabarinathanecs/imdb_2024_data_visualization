from sqlalchemy import create_engine
import pandas as pd

# Replace with your actual DB details
engine = create_engine("mysql+mysqlconnector://user:password@localhost/imdb2024")

df = pd.read_csv("../data/imdb_2024_movies.csv")
df.to_sql("movies", engine, if_exists="replace", index=False)

print("Data uploaded to SQL.")


