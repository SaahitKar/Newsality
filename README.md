### Newsality

#### Overview

This project fetches the latest business news headlines, analyzes their sentiment, and visualizes the sentiment distribution using **VADER Sentiment Analysis**. It then posts a summary of the sentiment analysis results to **Twitter** using the Tweepy API.

---

### Features

✔ Fetches **real-time news headlines** from [NewsAPI](https://newsapi.org/) ✔ **Sentiment analysis** using VADER (Positive, Neutral, Negative) ✔ Stores data in **CSV & SQLite database** ✔ **Data visualization** with Seaborn ✔ **Automated Twitter bot** that posts daily sentiment summary

---

### Technologies Used

- **Python** (requests, pandas, sqlite3, tweepy)
- **NewsAPI** (for fetching news headlines)
- **VADER Sentiment Analysis** (for sentiment scoring)
- **Matplotlib & Seaborn** (for data visualization)
- **Tweepy** (for Twitter API integration)

---

### Installation & Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-sentiment-analyzer.git
cd news-sentiment-analyzer
```

#### 2. Install Dependencies

```bash
pip install requests pandas sqlite3 tweepy vaderSentiment matplotlib seaborn
```

#### 3. Set Up API Keys

Create a `.env` file in the root directory and add:

```env
NEWS_API_KEY=your_newsapi_key
CONSUMER_KEY=your_twitter_consumer_key
CONSUMER_SECRET=your_twitter_consumer_secret
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

Alternatively, update `scraper.py` with your API keys.

#### 4. Run the Script

```bash
python scraper.py
```

---

### How It Works

1. Fetches news headlines from **NewsAPI**.
2. Saves headlines to **CSV & SQLite** for storage.
3. Analyzes sentiment using **VADER** and classifies as **Positive, Neutral, or Negative**.
4. Generates a **sentiment distribution plot**.
5. Tweets the summary of sentiment results on Twitter.

---

### Example Twitter Post

📢 **Today's News Sentiment Summary:**\
🔵 Positive: 12\
⚪ Neutral: 25\
🔴 Negative: 8

---

### Potential Improvements

🔹 Support more news categories (**politics, tech, entertainment**) 🔹 Improve accuracy with **machine learning-based sentiment analysis** 🔹 Deploy as a **daily scheduled job using AWS Lambda or GitHub Actions**

---

### License

📜 MIT License – Free to modify and use!
