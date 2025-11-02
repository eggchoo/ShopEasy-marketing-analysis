import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# def a function to fetch data from a SQL database using a SQL query
def fetch_data_from_sql():
    conn_str=(
        "Driver={SQL Server};"
        "Server=LAPTOP-I0KP3J1P\\SQLEXPRESS;"
        "Database=PortfolioProject_MarketingAnalytics;"
        "Trusted_Connection=yes;"  # Use Windows Authentication for the connection

    )
# Create a connection to the SQL Server
    conn = pyodbc.connect(conn_str)
# define the SQL query to fetch customer reviews data
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM dbo.customer_reviews"
# execute the query and fetch the data into a pandas DataFrame    
    df = pd.read_sql_query(query, conn)
# close the database connection
    conn.close()
    return df
customer_review_df=fetch_data_from_sql()

# Initialize the VADER sentiment intensity analyzer for analyzing the sentiment of text data
sia = SentimentIntensityAnalyzer()
# Define a function to calculate sentiment scores using VADER
def calculate_sentiment(review):
    # Get the sentiment scores for the review text
    sentiment = sia.polarity_scores(review)
    # Return the compound score, which is a normalized score between -1 (most negative) and 1 (most positive)
    return sentiment['compound']        

# Define a function to categorize sentiment using both the sentiment score and the review rating
def categorize_sentiment(score, rating):
    # Use both the text sentiment score and the numerical rating to determine sentiment category
    if score > 0.05:  # Positive sentiment score
        if rating >= 4:
            return 'Positive'  # High rating and positive sentiment
        elif rating == 3:
            return 'Mixed Positive'  # Neutral rating but positive sentiment
        else:
            return 'Mixed Negative'  # Low rating but positive sentiment
    elif score < -0.05:  # Negative sentiment score
        if rating <= 2:
            return 'Negative'  # Low rating and negative sentiment
        elif rating == 3:
            return 'Mixed Negative'  # Neutral rating but negative sentiment
        else:
            return 'Mixed Positive'  # High rating but negative sentiment
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'  # High rating with neutral sentiment
        elif rating <= 2:
            return 'Negative'  # Low rating with neutral sentiment
        else:
            return 'Neutral'  # Neutral rating with neutral sentiment


# Define a function to categorize sentiment into buckets
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'

# Apply sentiment calculation and categorization to the DataFrame
customer_review_df['SentimentScore'] = customer_review_df['ReviewText'].apply(calculate_sentiment)

# Apply sentiment categorization based on both sentiment score and rating
customer_review_df['SentimentCategory'] = customer_review_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)
# lambda row is short for 
# def temp_function(row):
#    return categorize_sentiment(row['SentimentScore'], row['Rating'])

# Apply sentiment bucketing to the DataFrame
customer_review_df['SentimentBucket'] = customer_review_df['SentimentScore'].apply(sentiment_bucket)    
# Display the first few rows of the DataFrame with sentiment scores, categories, and buckets
print(customer_review_df.head())
customer_review_df.to_csv('customer_reviews_with_sentiment.csv', index=False)
