from pytrends.request import TrendReq
import praw
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# ====== Reddit Config ======
CLIENT_ID = "an"
CLIENT_SECRET = "an"
USER_AGENT = "an"

def get_google_trends(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')
    data = pytrends.interest_over_time()
    if not data.empty:
        return data[keyword]
    return None

def get_reddit_mentions(keyword):
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    time_limit = datetime.utcnow() - timedelta(days=7)
    count = 0
    for submission in reddit.subreddit("all").search(keyword, sort="new", limit=100):
        created_time = datetime.utcfromtimestamp(submission.created_utc)
        if created_time > time_limit:
            count += 1
    return count

def compare_trends(keyword):
    google_data = get_google_trends(keyword)
    reddit_count = get_reddit_mentions(keyword)

    if google_data is None:
        print("No Google Trends data found.")
        return

    # Plot Google Trends (line)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    google_data.plot()
    plt.title("Google Trends: " + keyword)
    plt.xlabel("Date")
    plt.ylabel("Interest (0–100)")

    # Plot Reddit Mentions (bar)
    plt.subplot(1, 2, 2)
    plt.bar(["Reddit"], [reddit_count], color="tomato")
    plt.title("Reddit Mentions (7 Days)")
    plt.ylabel("Mentions")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    topic = input("Enter a topic to compare: ")
    compare_trends(topic)
