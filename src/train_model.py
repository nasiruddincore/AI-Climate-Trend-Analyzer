import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

def train_climate_model():
    print("🧠 Training Climate Forecasting Model...")
    df = pd.read_csv("data/climate_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Feature Engineering
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["DayOfYear"] = df["Date"].dt.dayofyear
    
    # Features (X) and Target (y)
    X = df[["Year", "Month", "DayOfYear", "CO2_ppm"]]
    y = df["Temperature_C"]
    
    # Split data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"📊 Model Performance -> MAE: {mae:.2f}°C | R² Score: {r2:.2f}")
    
    # Save Model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/climate_forecast_model.pkl")
    print("✅ Model saved to models/climate_forecast_model.pkl")

if __name__ == "__main__":
    train_climate_model()