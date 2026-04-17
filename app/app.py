import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import sys
import os

# Ensure src modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.feature_engine import create_features
from src.inventory_logic import calculate_inventory_metrics

st.set_page_config(page_title="Retail AI Optimizer", layout="wide")
st.title("🛒 Retail Sales Forecasting & Inventory Optimization")

@st.cache_data
def load_data():
    return pd.read_csv('data/historical_sales.csv')

df = load_data()

# Sidebar
st.sidebar.header("Settings")
selected_product = st.sidebar.selectbox("Select Product", df['Product'].unique())
current_stock = st.sidebar.number_input("Current Stock Level", min_value=0, value=150)

# Main Dashboard
st.subheader(f"Analytics for {selected_product}")

prod_df = df[df['Product'] == selected_product].copy()
prod_df['Date'] = pd.to_datetime(prod_df['Date'])

# Plot Historical Data
fig = px.line(prod_df[-90:], x='Date', y='Sales', title='Last 90 Days Sales Trend')
st.plotly_chart(fig, use_container_width=True)

# Forecasting Simulation
st.write("### AI Forecast & Inventory Recommendations")
if st.button("Generate Forecast & Plan"):
    # Load model
    model = joblib.load(f'models/xgb_{selected_product}.pkl')
    
    # Get last known data to predict next 7 days (Simplified for dashboard)
    featured_df = create_features(prod_df).tail(7)
    features = ['DayOfWeek', 'Month', 'Lag_1', 'Lag_7', 'Lag_14', 'Rolling_Mean_7']
    
    predictions = model.predict(featured_df[features])
    
    # Inventory Math
    lead_time = prod_df['LeadTime_Days'].iloc[0]
    hist_std = prod_df['Sales'].std()
    
    safety_stock, reorder_point = calculate_inventory_metrics(predictions, lead_time, hist_std)
    
    # Display Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Next 7-Day Demand (Est.)", int(predictions.sum()))
    col2.metric("Recommended Safety Stock", safety_stock)
    col3.metric("Reorder Point (ROP)", reorder_point)
    
    status = "🟢 Healthy" if current_stock > reorder_point else "🔴 Reorder NOW!"
    col4.metric("Current Status", status)

    if current_stock <= reorder_point:
        st.error(f"ALERT: Stock is below ROP. Order at least {reorder_point - current_stock + safety_stock} units immediately.")
