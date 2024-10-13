import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file with sentiments
df = pd.read_csv('c:/Users/Tarunjit/OneDrive/Desktop/safty_app/news_with_sentiments.csv')


st.title("News Sentiment Analysis Dashboard")
st.write("### Sentiment Distribution")
st.bar_chart(df['Sentiment'].value_counts())

# Generate word cloud
st.write("### Word Cloud of News Titles")
text = " ".join(title for title in df["Title"])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)



