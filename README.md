# 🛒 Retail Sales Forecasting & Inventory Optimization System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost%20(GPU)-orange.svg)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)

## 📌 Project Overview
This project is an end-to-end Machine Learning and Supply Chain Analytics solution designed to predict retail demand and optimize inventory levels. It prevents overstocking (saving capital) and understocking (preventing lost sales).

## 🏢 Business Value
- **Demand Forecasting:** Predicts next 7-day sales using lag features and rolling means.
- **Inventory Optimization:** Dynamically calculates Safety Stock and Reorder Points based on Lead Time Demand and historical variance.
- **Automated Alerts:** Triggers stock replenishment warnings.

## 🛠️ Tech Stack
- **Data Science:** Python, Pandas, NumPy
- **Machine Learning:** XGBoost (GPU Accelerated), Scikit-Learn
- **Web App & Deployment:** Streamlit, Plotly

## 🚀 How to Run Locally
1. Clone the repo: `git clone <your-repo-link>`
2. Install dependencies: `pip install -r requirements.txt`
3. Generate data: `python src/data_generator.py`
4. Train models: `python src/train_model.py`
5. Run Dashboard: `streamlit run app/app.py`

## 👨‍💻 Author
ASMIT SNAI

