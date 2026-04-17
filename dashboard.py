import streamlit as st
import requests
import pandas as pd

# FastAPI base URL
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="MON100 Dashboard", layout="wide")

st.title("MON100 ETF Dashboard")

# ---- Latest Data ----
st.header("Latest Data")

latest = requests.get(f"{BASE_URL}/latest").json()
latest = latest[-1]

st.metric("Market Price", latest["market_price"])
st.metric("iNAV", latest["inav_price"])
st.metric("Premium %", f"{latest['premium_percent']}%")

# ---- Trend ----
st.header("Trend")

trend = requests.get(f"{BASE_URL}/trend").json()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average", trend["average"])
col2.metric("Min", trend["min"])
col3.metric("Max", trend["max"])
col4.metric("Direction", trend["trend"])

# ---- History Chart ----
st.header("Premium Trend Chart")

history = requests.get(f"{BASE_URL}/history").json()

df = pd.DataFrame(history)

# convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# sort just in case
df = df.sort_values("timestamp")

st.line_chart(df.set_index("timestamp")["premium_percent"])
