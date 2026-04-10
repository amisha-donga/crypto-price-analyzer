import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/bitcoin_prices.csv")
# print(df)

df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])

df["moving_avg"] = df["price"].rolling(window=5).mean()

plt.figure(figsize=(10,5))
plt.plot(df["datetime"], df["price"], label="Price")
plt.plot(df["datetime"], df["moving_avg"], label="Moving Average")

plt.title("Bitcoin Price Trend")
plt.xlabel("Time")
plt.ylabel("Price")

plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()

plt.show()
