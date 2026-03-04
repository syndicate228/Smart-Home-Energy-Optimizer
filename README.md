# Smart-Home-Energy-Optimizer
IoT and Machine Learning based Home Energy Management System.
# 🏡 Smart Home Energy & Cost Optimizer

## 📌 Project Overview
This project is an IoT-enabled Home Energy Management System (HEMS) powered by Machine Learning. It utilizes a Multivariate Random Forest Regressor to predict total household electricity consumption based on historical smart meter data and real-time weather conditions (Temperature and Humidity).

## 🚀 Key Features
* **Predictive AI:** Forecasts power loads (in kW) using time-series and weather data.
* **Financial Optimization Engine:** Implements Time-of-Use (ToU) dynamic pricing logic to calculate exact Rupee (₹) savings.
* **Smart Load Shifting:** Automatically recommends shifting heavy appliance usage (e.g., Dishwashers) to off-peak hours to reduce grid strain.
* **Interactive UI:** Built with Streamlit, allowing users to manually adjust weather/time inputs to simulate different grid conditions.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Data Processing:** Pandas
* **Web UI:** Streamlit

## ⚙️ How to Run Locally
1. Clone this repository to your local machine.
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Run the Streamlit web application:
   `streamlit run app.py`
