import requests
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import tweepy.errors
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy

# Global variables needed for API
API_KEY = "8d58463e857142818643c743eb301607"
URL = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "category": "business",  # Change to "politics", "entertainment", etc.
    "apiKey": API_KEY
}

response = requests.get(URL, params=params)
analyzer = SentimentIntensityAnalyzer()

# Check if the request was successful
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    exit()

data = response.json()

# Ensure "articles" key exists
if "articles" not in data:
    print(f"Unexpected response format: {data}")
    exit()

# Extract headlines
headlines = [{"source": article["source"]["name"], "headline": article["title"], "url": article["url"]} for article in data["articles"]]

# Save to CSV
df = pd.DataFrame(headlines)
df.to_csv("news_headlines.csv", index=False)

# Store in SQLite
conn = sqlite3.connect("news.db")
df.to_sql("headlines", conn, if_exists="replace", index=False)
conn.close()

# Reload the data to process sentiment
df = pd.read_csv("news_headlines.csv")

# Compute sentiment scores
df["sentiment_score"] = df["headline"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])
df["sentiment"] = df["sentiment_score"].apply(lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral"))

# Save updated data
df.to_csv("news_sentiment.csv", index=False)
print(df.head())

# Define your Twitter API keys
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

positive_count = len(df[df["sentiment"] == "Positive"])
neutral_count = len(df[df["sentiment"] == "Neutral"])
negative_count = len(df[df["sentiment"] == "Negative"])

try:
    user = api.verify_credentials()
    if user:
        print(f"Authenticated as: {user.screen_name}")
    else:
        print("Authentication failed")
except tweepy.TweepyException as e:
    print(f"Error during authentication: {e}")
    exit()


summary = f"Today's News Sentiment:\n🔵 Positive: {positive_count}\n⚪ Neutral: {neutral_count}\n🔴 Negative: {negative_count}"
# api.update_status(summary)

# **Load the correct file with sentiment data**
df = pd.read_csv("news_sentiment.csv")

# **Plot sentiment distribution**
sns.countplot(x="sentiment", data=df, palette="coolwarm")
plt.title("Sentiment Distribution of News Headlines")
plt.show()
