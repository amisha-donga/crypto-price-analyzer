import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=60000, key="datarefresh")

st.title("Live Crypto Price Dashboard")

coin_dict = {
    "Bitcoin (BTC)" : "bitcoin",
    "Ethereum (ETH)" : "ethereum",
    "Litecoin (LTC)" : "litecoin"
}

selected_coin = st.selectbox("Select Cryptocurrency", list(coin_dict.keys()))
coin=coin_dict[selected_coin]

response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=1")
data = response.json()

if "prices" in  data:
    df = pd.DataFrame(data["prices"])
else:
    st.error("API Error : Could not fetch data")
    st.write(data)
    st.stop()

df.rename(columns={0:"timestamp", 1:"price"}, inplace=True)
df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")

df = df.set_index("datetime")

latest_price = df["price"].iloc[-1]
st.metric(label=f"Current {coin.capitalize()} Price", value=round(latest_price, 2))

alert_price =  st.number_input("Set Price Alert", value=70000)

if latest_price>alert_price:
    st.error("Price crossed your alert!")
else:
    st.success("Price is below alert level")

st.line_chart(df["price"])