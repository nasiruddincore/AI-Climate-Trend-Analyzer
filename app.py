import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
import os

st.set_page_config(page_title="Climate Trend Analyzer", page_icon="🌍", layout="wide")

st.title("🌍 AI Climate Trend Analyzer")
st.markdown("Analyze decades of historical climate data, detect extreme weather anomalies, and forecast future trends.")

# Validate Files
DATA_PATH = "data/climate_data.csv"
MODEL_PATH = "models/climate_forecast_model.pkl"

if not os.path.exists(DATA_PATH) or not os.path.exists(MODEL_PATH):
    st.error("⚠️ Data or Model missing. Please run `src/simulate_data.py` then `src/train_model.py` first.")
    st.stop()

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    # Anomaly Detection (Z-Score > 2.5 means it's an extreme outlier)
    mean_temp = df["Temperature_C"].mean()
    std_temp = df["Temperature_C"].std()
    df["Anomaly"] = np.where(abs((df["Temperature_C"] - mean_temp) / std_temp) > 2.5, "Extreme Event", "Normal")
    return df

df = load_data()
model = joblib.load(MODEL_PATH)

# --- KPI METRICS ---
st.markdown("### 📊 Overall Climate Indicators (Last 20 Years)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Global Temp", f"{df['Temperature_C'].mean():.2f} °C")
col2.metric("Max Temp Recorded", f"{df['Temperature_C'].max():.2f} °C", "Extreme Heat")
col3.metric("Current CO₂ Level", f"{df.iloc[-1]['CO2_ppm']:.0f} ppm", f"{(df.iloc[-1]['CO2_ppm'] - df.iloc[0]['CO2_ppm']):.0f} ppm rise")
col4.metric("Anomalies Detected", f"{len(df[df['Anomaly'] == 'Extreme Event'])} days")

st.divider()

# --- TREND VISUALIZATION ---
st.markdown("### 📈 Long-Term Temperature & Anomaly Tracking")
# Use a rolling average to smooth the noisy daily data
df_plot = df.copy()
df_plot["Temp_Rolling_365"] = df_plot["Temperature_C"].rolling(window=365).mean()

fig1 = go.Figure()
# Base Trend
fig1.add_trace(go.Scatter(x=df_plot["Date"], y=df_plot["Temp_Rolling_365"], mode='lines', name='Yearly Moving Avg', line=dict(color='orange', width=2)))
# Anomalies
anomalies = df_plot[df_plot["Anomaly"] == "Extreme Event"]
fig1.add_trace(go.Scatter(x=anomalies["Date"], y=anomalies["Temperature_C"], mode='markers', name='Extreme Anomalies', marker=dict(color='red', size=6, symbol='x')))

fig1.update_layout(height=400, xaxis_title="Year", yaxis_title="Temperature (°C)")
st.plotly_chart(fig1, use_container_width=True)

# --- CORRELATION & FORECASTING ---
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### ☁️ CO₂ vs Temperature Correlation")
    fig2 = px.scatter(df, x="CO2_ppm", y="Temperature_C", color="Anomaly", color_discrete_map={"Normal": "#1E90FF", "Extreme Event": "red"}, opacity=0.5)
    st.plotly_chart(fig2, use_container_width=True)

with col_b:
    st.markdown("### 🔮 Predict Future Temperature")
    st.info("Simulate future conditions to see the AI's temperature projection.")
    
    future_year = st.slider("Select Future Year", 2025, 2050, 2030)
    future_co2 = st.number_input("Estimated CO₂ (ppm)", min_value=400, max_value=600, value=450)
    future_month = st.selectbox("Select Month", range(1, 13), format_func=lambda x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][x-1])
    
    if st.button("Generate AI Forecast"):
        # Predict using [Year, Month, DayOfYear, CO2]
        pred_temp = model.predict([[future_year, future_month, 15, future_co2]])[0]
        st.success(f"**Forecasted Average Temperature for {future_month}/{future_year}:** {pred_temp:.2f} °C")