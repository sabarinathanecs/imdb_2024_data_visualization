from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

# Set path to chromedriver.exe
CHROMEDRIVER_PATH = "C:\WebDriver"  
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Create data folder if not exists
if not os.path.exists("../data"):
    os.makedirs("../data")

# Open IMDb search page
driver.get("https://www.imdb.com/search/title/?year=2024&title_type=feature")
time.sleep(3)  # Let page load

# Initialize lists to hold data
movie_names, genres, ratings, votes, durations = [], [], [], [], []

# Find all movie containers
movies = driver.find_elements(By.CLASS_NAME, "lister-item")

for movie in movies:
    try:
        title = movie.find_element(By.TAG_NAME, "h3").text.split("\n")[0]
        genre = movie.find_element(By.CLASS_NAME, "genre").text.strip().split(",")[0]
        rating = movie.find_element(By.CLASS_NAME, "ratings-imdb-rating").text.strip()
        vote = movie.find_element(By.XPATH, './/p[@class="sort-num_votes-visible"]/span[2]').text.replace(',', '')
        duration = movie.find_element(By.CLASS_NAME, "runtime").text.replace(' min', '')

        # Append data to lists
        movie_names.append(title)
        genres.append(genre)
        ratings.append(float(rating))
        votes.append(int(vote))
        durations.append(int(duration))

    except Exception:
        continue  # Skip movies with missing info

# Close browser
driver.quit()

# Save data to DataFrame
df = pd.DataFrame({
    "Movie Name": movie_names,
    "Genre": genres,
    "Ratings": ratings,
    "Voting Counts": votes,
    "Duration": durations
})

# Save to CSV
df.to_csv("../data/imdb_2024_movies.csv", index=False)
print("✅ Scraping completed and CSV saved to /data")

