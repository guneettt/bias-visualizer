from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def get_google_trends(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')
    data = pytrends.interest_over_time()
    if not data.empty:
        return data[keyword]
    return None

def compare_trends(keyword):
    google_data = get_google_trends(keyword)

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

    plt.subplot(1, 2, 2)
    plt.ylabel("Mentions")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    topic = input("Enter a topic to compare: ")
    compare_trends(topic)
