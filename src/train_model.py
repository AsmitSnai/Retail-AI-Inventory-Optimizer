import pandas as pd
import xgboost as xgb
import joblib
import os
from feature_engine import create_features

def train_and_save():
    df = pd.read_csv('data/historical_sales.csv')
    df_featured = create_features(df)
    
    # We will train one model per product for simplicity in this portfolio
    os.makedirs('models', exist_ok=True)
    
    features = ['DayOfWeek', 'Month', 'Lag_1', 'Lag_7', 'Lag_14', 'Rolling_Mean_7']
    
    for product in df_featured['Product'].unique():
        prod_data = df_featured[df_featured['Product'] == product]
        X = prod_data[features]
        y = prod_data['Sales']
        
        # Split train/test (last 30 days as test)
        X_train, X_test = X[:-30], X[-30:]
        y_train, y_test = y[:-30], y[-30:]
        
        # XGBoost with GPU acceleration
        model = xgb.XGBRegressor(
            n_estimators=100, 
            learning_rate=0.1, 
            device='cuda', # Enables GPU
            objective='reg:squarederror'
        )
        model.fit(X_train, y_train)
        
        joblib.dump(model, f'models/xgb_{product}.pkl')
        print(f"Model trained and saved for {product}")

if __name__ == "__main__":
    train_and_save()
