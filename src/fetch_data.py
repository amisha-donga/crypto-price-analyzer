import requests
import pandas as pd

response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1")
# print(response.status_code)

data = response.json()
# print(data)

df = pd.DataFrame(data["prices"])
# print(df)

df.rename(columns={0:"timestamp", 1:"price"}, inplace=True)

temp_dt = pd.to_datetime(df["timestamp"], unit="ms")
df["date"] = temp_dt.dt.strftime("%Y-%m-%d")
df["time"] = temp_dt.dt.strftime("%H:%M:%S")

# df["date"] = pd.to_datetime(df["date"], unit="ms").dt.date
df["price"] = df["price"].map("{:.2f}".format)

df = df.drop(columns=["timestamp"])

df = df[["date", "time", "price"]]

df.to_csv("data/bitcoin_prices.csv", index=False)

print("\n", df.head())