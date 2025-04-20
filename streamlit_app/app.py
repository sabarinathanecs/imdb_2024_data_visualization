import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_csv("../data/imdb_2024_movies.csv")

st.title("🎬 IMDb 2024 Movie Dashboard")

# Filters
st.sidebar.header("Filter Options")
genres = st.sidebar.multiselect("Genres", df["Genre"].unique())
ratings = st.sidebar.slider("Ratings", 0.0, 10.0, (6.0, 10.0))
votes = st.sidebar.slider("Voting Counts", 0, 200000, (0, 200000))
duration = st.sidebar.slider("Duration (min)", 30, 240, (60, 180))

filtered = df[
    df["Ratings"].between(*ratings) &
    df["Voting Counts"].between(*votes) &
    df["Duration"].between(*duration)
]

if genres:
    filtered = filtered[filtered["Genre"].isin(genres)]

st.subheader("🎞 Filtered Movies")
st.dataframe(filtered)

st.subheader("⭐ Top 10 Rated Movies")
st.dataframe(df.sort_values(by=["Ratings", "Voting Counts"], ascending=False).head(10))

st.subheader("📊 Genre Distribution")
fig1, ax1 = plt.subplots()
df["Genre"].value_counts().plot(kind='bar', ax=ax1)
st.pyplot(fig1)

