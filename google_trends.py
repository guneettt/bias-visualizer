from pytrends.request import TrendReq
from datetime import datetime, timedelta

pytrends = TrendReq(hl='en-US', tz=360)

def fetch_google_trends(keyword: str):
    # Fetch ~3 months of daily data
    pytrends.build_payload([keyword], cat=0, timeframe='today 3-m', geo='', gprop='')

    df = pytrends.interest_over_time()

    if df.empty:
        print("⚠️ No data returned for keyword:", keyword)
        return []

    # Keep only last 7 days (grouped by day if needed)
    df = df.tail(7)

    timeline = []
    for date, row in df.iterrows():
        timeline.append({
            "time": date.strftime('%Y-%m-%d'),
            "value": int(row[keyword])
        })

    return timeline
