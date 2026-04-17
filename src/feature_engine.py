import pandas as pd

def create_features(df):
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by=['Product', 'Date'])
    
    # Time based features
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month
    
    # Lag features (Sales from previous days)
    for i in [1, 7, 14]:
        df[f'Lag_{i}'] = df.groupby('Product')['Sales'].shift(i)
        
    # Rolling averages
    df['Rolling_Mean_7'] = df.groupby('Product')['Sales'].transform(lambda x: x.shift(1).rolling(window=7).mean())
    
    # Drop NaNs created by lagging
    df = df.dropna()
    return df