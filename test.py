from reddit_scraper import fetch_reddit_data

topic = "elon musk"
print("Fetching Reddit mentions for:", topic)
count = fetch_reddit_data(topic)
print("Mentions in last 7 days:", count)
