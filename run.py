"""
run.py

Main script for cleaning and analyzing customer feedback data.
"""

import pandas as pd
from src.data_cleaning import load_raw_data, clean_feedback_data
from src.analysis import calculate_daily_satisfaction, extract_top_keywords, find_most_positive_day

def main():
    """
    Main pipeline for customer feedback analysis.
    """
    # Step 1: Load raw data
    raw_file_path = "data/raw/customer_feedback.csv"
    
    raw_df = load_raw_data(raw_file_path)
    
    if raw_df is None:
        return

    # Step 2: Clean data
    cleaned_df = clean_feedback_data(raw_df)

    # Step 3: Calculate daily satisfaction
    daily_satisfaction = calculate_daily_satisfaction(cleaned_df)

    # Step 4: Extract top keywords
    top_keywords = extract_top_keywords(cleaned_df)

    # Step 5: Identify most positive day
    most_positive_day = find_most_positive_day(daily_satisfaction)

    # Prepare cleaned feedback table with new column order
    cleaned_table = cleaned_df[["date", "time", "feedback_clean", "satisfaction"]]

    # Create visualization section as a DataFrame
    visualization_data = [
        ["", "", "Top 3 Keywords:", ""],
        ["", "", f"- excellent: {next(count for word, count in top_keywords if word == 'excellent')} occurrences", ""],
        ["", "", f"- great: {next(count for word, count in top_keywords if word == 'great')} occurrences", ""],
        ["", "", f"- service: {next(count for word, count in top_keywords if word == 'service')} occurrences", ""],
        ["", "", "Most Positive Day:", ""],
        ["", "", f"- {most_positive_day['date']} (Avg Satisfaction: {most_positive_day['average_satisfaction']:.1f})", ""]
    ]
    
    # Match visualization columns to cleaned table columns
    visualization_df = pd.DataFrame(visualization_data, columns=cleaned_table.columns)

    # Combine cleaned table and visualization
    final_df = pd.concat([cleaned_table, visualization_df], ignore_index=True)

    # Save to CSV
    final_df.to_csv("data/interim/cleaned_feedback.csv", index=False)

if __name__ == "__main__":
    main()
