import praw
from datetime import datetime, timedelta

# ✅ Define reddit at module level
reddit = praw.Reddit(
    client_id="fv6tgPssxe9R3jqfAAMPLA",
    client_secret="Vgzta3doB218Uf90_Epl7UROzRbPA",
    user_agent="Significant_Camp_700",
    username="Significant_Camp_700",
    password="Harrypotter@007"
)

def fetch_reddit_data(keyword: str) -> int:
    time_limit = datetime.utcnow() - timedelta(days=7)
    count = 0

    try:
        for submission in reddit.subreddit("all").search(keyword, sort="new", limit=100):
            created_time = datetime.utcfromtimestamp(submission.created_utc)
            if created_time > time_limit:
                count += 1
    except Exception as e:
        print("❌ Reddit fetch error:", str(e))

    return count

if __name__ == "__main__":
    # ✅ Now reddit is accessible here
    for submission in reddit.subreddit("worldnews").hot(limit=1):
        print(submission.title)
