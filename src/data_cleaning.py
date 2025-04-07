import pandas as pd

def load_raw_data(file_path):
    """
    Load raw customer feedback data from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("Raw data loaded successfully!")
        return df
    except FileNotFoundError:
        print("Error: File not found. Check the path to your CSV.")
        return None

def clean_feedback_data(df):
    """
    Clean and preprocess customer feedback data with robust error handling.
    
    Args:
        df (pd.DataFrame): Raw input data
        
    Returns:
        pd.DataFrame: Cleaned data with columns:
            - date (str): DD/MM/YYYY format
            - time (str): HH:MM:SS format
            - feedback_clean (str): Normalized text
            - satisfaction (float): Numeric rating
    """
    # 1. Empty Input Handling
    if df.empty or "feedback" not in df.columns:
        return pd.DataFrame(columns=["date", "time", "feedback_clean", "satisfaction"])

    # 2. Handle Missing Values
    df = df.dropna(subset=["timestamp", "feedback"]).copy()

    # 3. Initialize Missing Columns
    if "satisfaction" not in df.columns:
        df["satisfaction"] = np.nan

    # 4. Safe Type Conversion for Feedback
    df.loc[:, "feedback"] = df["feedback"].astype(str)

    # 5. Text Normalization
    df.loc[:, "feedback_clean"] = (
        df["feedback"]
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
    )

    # 6. DateTime Parsing
    df.loc[:, "datetime"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
        dayfirst=True  # Ensures DD/MM/YYYY format is handled correctly
    )

    # 7. Remove Invalid Dates
    df = df.dropna(subset=["datetime"]).copy()

    # 8. Split DateTime Columns
    df.loc[:, "date"] = df["datetime"].dt.strftime("%d/%m/%Y")
    df.loc[:, "time"] = df["datetime"].dt.strftime("%H:%M:%S")

    # 9. Final Column Selection
    final_columns = ["date", "time", "feedback_clean", "satisfaction"]
    return df[final_columns]

    """
    Clean and preprocess customer feedback data.
    """
    # Handle missing values
    df = df.dropna(subset=["timestamp", "feedback"]).copy()
    df.loc[:, "satisfaction"] = df["satisfaction"].fillna(df["satisfaction"].median())

    # Normalize feedback text
    df.loc[:, "feedback_clean"] = (
        df["feedback"].str.lower().str.replace(r"[^\w\s]", "", regex=True)
    )

    # Convert timestamp to datetime (FIXED: Added dayfirst=True)
    df.loc[:, "datetime"] = pd.to_datetime(
        df["timestamp"], 
        errors="coerce", 
        dayfirst=True  # Explicitly handle DD/MM format
    )
    df = df.dropna(subset=["datetime"]).copy()

    # Split datetime into date/time columns
    df.loc[:, "date"] = df["datetime"].dt.strftime("%d/%m/%Y")
    df.loc[:, "time"] = df["datetime"].dt.strftime("%H:%M:%S")

    return df

def save_cleaned_data(df, output_path):
    """
    Save cleaned data to a CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

    """
    Clean and preprocess customer feedback data with robust error handling.
    
    Args:
        df (pd.DataFrame): Raw input data
        
    Returns:
        pd.DataFrame: Cleaned data with columns:
            - date (str): DD/MM/YYYY format
            - time (str): HH:MM:SS format
            - feedback_clean (str): Normalized text
            - satisfaction (float): Numeric rating
    """
    # 1. Empty Input Handling
    if df.empty or "feedback" not in df.columns:
        return pd.DataFrame(columns=["date", "time", "feedback_clean", "satisfaction"])

    # 2. Handle Missing Values
    df = df.dropna(subset=["timestamp", "feedback"]).copy()

    # 3. Initialize Missing Columns
    if "satisfaction" not in df.columns:
        df["satisfaction"] = np.nan

    # 4. Safe Type Conversion for Feedback
    df.loc[:, "feedback"] = df["feedback"].astype(str)

    # 5. Text Normalization
    df.loc[:, "feedback_clean"] = (
        df["feedback"]
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
    )

    # 6. DateTime Parsing
    df.loc[:, "datetime"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
        dayfirst=True  # Ensures DD/MM/YYYY format is handled correctly
    )

    # 7. Remove Invalid Dates
    df = df.dropna(subset=["datetime"]).copy()

    # 8. Split DateTime Columns
    df.loc[:, "date"] = df["datetime"].dt.strftime("%d/%m/%Y")
    df.loc[:, "time"] = df["datetime"].dt.strftime("%H:%M:%S")

    # 9. Final Column Selection
    final_columns = ["date", "time", "feedback_clean", "satisfaction"]
    return df[final_columns]
