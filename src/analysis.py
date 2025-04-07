from collections import Counter

def add_sentiment_column(df):
    """
    Map satisfaction scores to sentiment categories.
    """
    sentiment_map = {
        1: "Negative",
        2: "Negative",
        3: "Neutral",
        4: "Positive",
        5: "Positive",
    }
    df["sentiment"] = df["satisfaction"].map(sentiment_map)
    return df

def calculate_daily_satisfaction(df):
    """
    Calculate average satisfaction scores for each day.
    """
    daily_satisfaction = (
        df.groupby("date")["satisfaction"]
        .mean()
        .reset_index()
        .rename(columns={"satisfaction": "average_satisfaction"})
    )
    return daily_satisfaction

def extract_keywords(df, top_n=10):
    """
    Extract top keywords from cleaned feedback using TF-IDF.
    """
    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df["feedback_clean"])

    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    keyword_scores = list(zip(feature_names, tfidf_scores))
    sorted_keywords = sorted(keyword_scores, key=lambda x: x[1], reverse=True)
    
    return sorted_keywords[:top_n]

def extract_top_keywords(df, top_n=3):
    """
    Extract top N most common keywords from feedback text.
    """
    all_words = ' '.join(df['feedback_clean']).split()
    word_counts = Counter(all_words)
    return word_counts.most_common(top_n)

def find_most_positive_day(daily_satisfaction):
    """
    Identify the day with the highest average satisfaction rating.
    """
    return daily_satisfaction.loc[daily_satisfaction["average_satisfaction"].idxmax()]
