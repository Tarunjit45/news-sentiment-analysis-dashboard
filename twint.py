import twint

# Configure Twint
c = twint.Config()
c.Search = "AI"  # Your search term
c.Limit = 100  # Number of tweets to scrape
c.Store_csv = True  # Save to CSV
c.Output = "tweets.csv"  # File name for output

# Run Twint
twint.run.Search(c)
