from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  

def analyze_sentiment(text):  
    """  
    Calculate sentiment scores using VADER.  
    Args:  
        text (str): Input feedback text.  
    Returns:  
        dict: Sentiment scores (neg, neu, pos, compound).  
    """  
    analyzer = SentimentIntensityAnalyzer()  
    return analyzer.polarity_scores(text)  

def apply_sentiment_analysis(df):  
    """  
    Add sentiment columns to DataFrame.  
    """  
    scores = df['cleaned_feedback'].apply(analyze_sentiment).apply(pd.Series)  
    return pd.concat([df, scores], axis=1)  

# Example usage  
df = pd.read_csv("../data/interim/cleaned_feedback.csv")  
df = apply_sentiment_analysis(df)  
df.to_csv("../data/processed/analyzed_feedback.csv", index=False)  
