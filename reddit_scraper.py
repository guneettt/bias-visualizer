import praw
from datetime import datetime, timedelta

CLIENT_ID = "ab"
CLIENT_SECRET = "ab"
USER_AGENT = "an"

def fetch_reddit_data(keyword):
    # Set up Reddit API connection
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    # Time window: last 7 days
    time_limit = datetime.utcnow() - timedelta(days=7)
    count = 0
    posts = []

    # Search in popular subreddits
    for submission in reddit.subreddit("all").search(keyword, sort="new", limit=100):
        created_time = datetime.utcfromtimestamp(submission.created_utc)
        if created_time > time_limit:
            count += 1
            posts.append((submission.title, created_time.strftime("%Y-%m-%d %H:%M")))

    print(f"\nReddit mentions of '{keyword}' in last 7 days: {count}")
    for title, time in posts[:5]:  # show only top 5
        print(f"- [{time}] {title}")

if __name__ == "__main__":
    topic = input("Enter a keyword/topic: ")
    fetch_reddit_data(topic)
# This script fetches Reddit posts mentioning a given keyword or topic in the last 7 days.