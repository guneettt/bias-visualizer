from pytrends.request import TrendReq

def fetch_google_trends(keyword: str) -> int:
    pytrends = TrendReq(hl='en-US', tz=360, retries=3, backoff_factor=2)
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')
    data = pytrends.interest_over_time()
    
    if not data.empty:
        return int(data[keyword].mean())  # Return average interest over time
    else:
        return 0

if __name__ == "__main__":
    topic = input("Enter a keyword/topic: ")
    fetch_google_trends(topic)
# This script fetches Google Trends data for a given keyword or topic.
