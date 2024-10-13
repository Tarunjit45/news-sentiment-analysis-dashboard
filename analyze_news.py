import pandas as pd
from textblob import TextBlob

# Load the CSV file
df = pd.read_csv('news_articles.csv')

# Perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text).sentiment.polarity
    if analysis > 0:
        return 'Positive'
    elif analysis < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Title'].apply(get_sentiment)

# Print sentiment counts
print(df['Sentiment'].value_counts())

# Save updated data with sentiments
df.to_csv('news_with_sentiments.csv', index=False)
print("Sentiment analysis completed and saved.")

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Combine all titles into a single string
text = " ".join(title for title in df["Title"])

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
