from pytrends.request import TrendReq

def fetch_google_trends(keyword):
    pytrends = TrendReq(hl='en-US', tz=360, retries=3, backoff_factor=2)
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')
    
    data = pytrends.interest_over_time()
    if not data.empty:
        data = data.drop(columns=["isPartial"])
        print("Google Trends data for:", keyword)
        print(data.tail())  # Show last few rows
    else:
        print("No data found.")

if __name__ == "__main__":
    topic = input("Enter a keyword/topic: ")
    fetch_google_trends(topic)
# This script fetches Google Trends data for a given keyword or topic.