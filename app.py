import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

# Setup the Web Page
st.set_page_config(page_title="Smart HEMS", layout="centered")
st.title("🏡 Smart Home Energy & Cost Optimizer")
st.write("Multivariate AI predicting energy loads based on real-time weather and ToU Tariffs.")

# Load Data and Train the AI
@st.cache_resource
def load_and_train():
    df = pd.read_csv('HomeC.csv', low_memory=False).dropna()
    df['Datetime'] = pd.to_datetime(df['time'], unit='s')
    df['Hour'] = df['Datetime'].dt.hour
    df['Day_of_Week'] = df['Datetime'].dt.dayofweek
    df['Month'] = df['Datetime'].dt.month
    
    X = df[['Hour', 'Day_of_Week', 'Month', 'temperature', 'humidity']]
    y = df['use [kW]']
    
    model = RandomForestRegressor(n_estimators=10, random_state=42, n_jobs=-1)
    model.fit(X, y)
    return model

with st.spinner("Booting up Multivariate AI..."):
    model = load_and_train()
st.success("✅ Smart Home AI Loaded!")

# User Interface
st.header("🌦️ Enter Current Conditions")

col1, col2 = st.columns(2)
with col1:
    hour = st.slider("Hour of Day (0-23)", 0, 23, 18)
    month = st.slider("Month (1-12)", 1, 12, 7)
with col2:
    temp = st.slider("Temperature (°C)", 10.0, 45.0, 35.0)
    hum = st.slider("Humidity", 0.1, 1.0, 0.60)

# Optimization Engine
if st.button("Run Financial Optimization"):
    prediction = model.predict([[hour, 2, month, temp, hum]])[0]
    
    st.markdown("---")
    st.subheader(f"⚡ Predicted Home Load: **{prediction:.2f} kW**")
    
    peak_hours = [17, 18, 19, 20, 21]
    peak_rate = 12.0
    off_peak_rate = 5.0
    dishwasher_load = 1.5 
    
    if hour in peak_hours:
        savings = (dishwasher_load * peak_rate) - (dishwasher_load * off_peak_rate)
        st.error("🔴 **HIGH TARIFF PERIOD (PEAK HOURS)**")
        st.write(f"Current Rate: **₹{peak_rate}/kWh**")
        st.write("👉 **Action:** Delay Dishwasher (1.5 kW) to after 10:00 PM.")
        st.subheader(f"💰 **Guaranteed Savings: ₹{savings:.2f}**")
    else:
        st.success("🟢 **LOW TARIFF PERIOD (OFF-PEAK)**")
        st.write(f"Current Rate: **₹{off_peak_rate}/kWh**")
        st.write("👉 **Action:** Rates are cheap. Safe to run heavy appliances.")
