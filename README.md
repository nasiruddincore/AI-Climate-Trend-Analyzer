# 🌍 AI-Powered Climate Trend Analyzer

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Frontend](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

An industry-oriented data science project designed to analyze decades of historical climate data. This system filters out daily weather noise to uncover true global warming trends, flags extreme weather anomalies using statistical thresholds, and utilizes Machine Learning to forecast future temperatures based on carbon emissions.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [System Objectives](#-system-objectives)
- [Industry Relevance & Use Cases](#-industry-relevance--use-cases)
- [Architecture & Data Flow](#-architecture--data-flow)
- [Folder Structure](#-folder-structure)
- [Installation & Setup Guide](#-installation--setup-guide)
- [How to Run (Execution Workflow)](#-how-to-run-execution-workflow)
- [Model Evaluation Results](#-model-evaluation-results)
- [Author & License](#-author--license)

---

## 📌 Project Overview
Climate change requires data-driven policy making, but raw environmental data is incredibly noisy and volatile. This project uses a Random Forest neural network to study simulated historical climate data and forecast future environmental states. The trained model is deployed through an interactive web dashboard, enabling researchers and city planners to run dynamic scenario simulations.

---

## ⚠️ Problem Statement
* **Extreme Weather Risks:** Unpredictable climate spikes (heatwaves, droughts) catch municipalities off-guard, leading to infrastructure failures and agricultural losses.
* **Data Noise:** Daily and seasonal weather fluctuations make it difficult to visualize and prove long-term global warming trajectories.
* **Data Access Barriers:** Accessing pristine, multi-decade climatology databases can be difficult for students. This project solves this via a realistic time-series environmental simulation engine.

---

## 🎯 System Objectives
1. **Virtual Telemetry Generation:** Simulate 20 years of continuous daily climate data, mathematically incorporating seasonality, global warming slopes, and random anomalies.
2. **Time-Series Feature Extraction:** Construct rolling averages and datetime indices (Year, Month, Day of Year) to capture temporal behaviors.
3. **Anomaly Detection:** Implement Z-Score statistical thresholds to automatically flag days with dangerous, record-breaking temperatures.
4. **Predictive Modeling:** Train a Scikit-Learn Random Forest Regressor to predict future temperatures based on CO₂ inputs, achieving an $R^2$ accuracy score above 0.85.
5. **Interactive Simulation UI:** Provide a Streamlit dashboard for real-time scenario stress-testing (e.g., forecasting 2040 temperatures under high CO₂ conditions).

---

## 🏭 Industry Relevance & Use Cases
* **Smart City Planners:** Prepares urban infrastructure (cooling centers, storm drains) for predicted severe weather trends.
* **Agritech & Farming:** Forecasts long-term temperature and rainfall shifts to optimize crop cycles and water reservoir management.
* **Environmental Agencies:** Tracks and visualizes the direct correlation between rising CO₂ emissions and global temperature baselines to guide carbon-reduction policies.

---

## 📐 Architecture & Data Flow

```text
[ Virtual Climate Simulator ] ──(Simulated Telemetry)──► [ data/climate_data.csv ]
                                                                 │
                                                       (Feature Engineering)
                                                                 ▼
[ Streamlit UI Dashboard ] ◄──────(Inference)───────── [ Random Forest ML Model ]
📂 Folder Structure
Plaintext

AI-Climate-Trend-Analyzer/
│
├── assets/                  # Proof-of-work screenshots for GitHub
│   ├── dashboard_kpis.png
│   ├── trend_and_anomalies.png
│   └── forecast_ui.png
│
├── data/                    # Storage for raw and generated CSV telemetry
│   └── climate_data.csv
│
├── models/                  # Serialized trained ML models
│   └── climate_forecast_model.pkl
│
├── src/                     # Core modular Python logic
│   ├── simulate_data.py     # Generates the synthetic climate dataset
│   └── train_model.py       # ML training and evaluation pipeline
│
├── app.py                   # Main Streamlit web application
├── requirements.txt         # Package dependency manifest
├── .gitignore               # Prevents tracking virtualenv and raw outputs
└── README.md                # Project documentation

⚙️ Installation & Setup Guide

1. Clone the Repository
Bash

git clone [https://github.com/YOUR_USERNAME/AI-Climate-Trend-Analyzer.git](https://github.com/YOUR_USERNAME/AI-Climate-Trend-Analyzer.git)
cd AI-Climate-Trend-Analyzer

2. Create a Virtual Environment
Bash

python -m venv venv

# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3. Install Dependencies
Bash

pip install -r requirements.txt

🚀 How to Run (Execution Workflow)

Step 1: Generate Climate Data

Creates 20 years (7,300 days) of continuous daily weather logs.
Bash

python src/simulate_data.py

Step 2: Train the AI Forecasting Model

Extracts temporal features, engineers rolling averages, and trains the Random Forest Regressor.
Bash

python src/train_model.py

Step 3: Launch Web Dashboard Simulation

Starts the interactive UI for visualization, anomaly tracking, and future forecasting.
Bash

streamlit run app.py

Navigate to http://localhost:8501 in your web browser to view the application.
📊 Model Evaluation Results

    Mean Absolute Error (MAE): ~1.54 °C

    R² Score (Accuracy): ~0.88

👤 Author & License

Developed as an industry-oriented Data Science & Environmental Analytics portfolio project. Distributed under the MIT License.
