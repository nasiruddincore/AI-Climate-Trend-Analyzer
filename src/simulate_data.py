import pandas as pd
import numpy as np
import os

def generate_climate_data(years=20):
    print("🌍 Generating decades of climate data...")
    np.random.seed(42)
    
    # Generate 20 years of daily dates
    dates = pd.date_range(start="2004-01-01", periods=years*365, freq="D")
    df = pd.DataFrame({"Date": dates})
    
    # Time features
    days_passed = np.arange(len(df))
    day_of_year = df["Date"].dt.dayofyear
    
    # 1. Temperature: Base 15°C + Seasonality (Sine wave) + Global Warming Trend + Noise
    seasonality = 10 * np.sin(2 * np.pi * (day_of_year - 100) / 365) # Hot in summer, cold in winter
    warming_trend = 0.0002 * days_passed # Gradual increase over time
    noise = np.random.normal(0, 2, len(df))
    df["Temperature_C"] = 15 + seasonality + warming_trend + noise
    
    # 2. CO2 Levels: Base 380 ppm + Upward trend + Minor seasonal cycle
    co2_trend = 380 + (0.005 * days_passed)
    co2_seasonality = 3 * np.sin(2 * np.pi * day_of_year / 365)
    df["CO2_ppm"] = co2_trend + co2_seasonality + np.random.normal(0, 1, len(df))
    
    # 3. Rainfall (mm): Random with seasonal variation
    rain_base = np.maximum(0, np.random.normal(2, 5, len(df)))
    rain_season = np.maximum(0, 5 * np.cos(2 * np.pi * day_of_year / 365))
    df["Rainfall_mm"] = np.round(rain_base + rain_season, 2)
    
    # Inject Extreme Weather Anomalies (Heatwaves)
    anomaly_indices = np.random.choice(len(df), size=30, replace=False)
    df.loc[anomaly_indices, "Temperature_C"] += np.random.uniform(7, 12, size=30) # Sudden temp spikes
    
    # Save to data folder
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/climate_data.csv", index=False)
    print(f"✅ Generated {len(df)} days of data at data/climate_data.csv")

if __name__ == "__main__":
    generate_climate_data()