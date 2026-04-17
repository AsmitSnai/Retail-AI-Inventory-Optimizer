import numpy as np

def calculate_inventory_metrics(forecasted_demand_next_7_days, lead_time_days, historical_sales_std):
    # Daily averages
    avg_daily_demand = np.mean(forecasted_demand_next_7_days)
    
    # Safety Stock formula: Z * std_dev * sqrt(lead_time)
    # Z = 1.65 represents a 95% service level
    z_score = 1.65 
    safety_stock = z_score * historical_sales_std * np.sqrt(lead_time_days)
    
    # Reorder Point = Lead Time Demand + Safety Stock
    lead_time_demand = avg_daily_demand * lead_time_days
    reorder_point = lead_time_demand + safety_stock
    
    return int(np.ceil(safety_stock)), int(np.ceil(reorder_point))