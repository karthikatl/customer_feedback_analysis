def daily_satisfaction(df):  
    """  
    Calculate average satisfaction per day.  
    """  
    return df.groupby('date')['satisfaction'].mean().reset_index()  

# Example usage  
daily_avg = daily_satisfaction(df)  
print(daily_avg)  
