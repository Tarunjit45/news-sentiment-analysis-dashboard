import requests

# NewsAPI Setup
API_KEY = 'd5eac5462bac4273808c8a9f722a9b18'  # Replace with your NewsAPI key
url = f"https://newsapi.org/v2/everything?q=AI&apiKey={API_KEY}"

# Fetch Data from NewsAPI
response = requests.get(url)
data = response.json()

# Check for successful response
if data['status'] == 'ok':
    print(f"Total Articles Found: {data['totalResults']}\n")

    # Save articles to CSV
    with open("news_articles.csv", "w", encoding="utf-8") as f:
        f.write("Title,Description,URL\n")
        for article in data['articles']:
            title = article['title'].replace(",", " ")
            description = article['description'].replace(",", " ")
            url = article['url']
            f.write(f"{title},{description},{url}\n")

    print("Articles saved to 'news_articles.csv'")
else:
    print("Failed to fetch articles:", data['message'])
