import pandas as pd
import numpy as np
import os

def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start='2022-01-01', end='2023-12-31')
    products = ['Laptop', 'Smartphone', 'Headphones']
    
    data = []
    for product in products:
        base_sales = {'Laptop': 20, 'Smartphone': 50, 'Headphones': 100}[product]
        for date in dates:
            # Add weekend bump and random noise
            weekend_factor = 1.5 if date.weekday() >= 5 else 1.0
            sales = int(max(0, np.random.normal(base_sales * weekend_factor, base_sales * 0.2)))
            
            data.append({
                'Date': date,
                'Product': product,
                'Sales': sales,
                'Price': {'Laptop': 1000, 'Smartphone': 800, 'Headphones': 150}[product],
                'LeadTime_Days': {'Laptop': 7, 'Smartphone': 5, 'Headphones': 3}[product]
            })
            
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/historical_sales.csv', index=False)
    print("Dataset generated successfully at data/historical_sales.csv")

if __name__ == "__main__":
    generate_data()