import pandas as pd

df = pd.read_csv("data/bitcoin_prices.csv", encoding="utf-8")

avg_price = df["price"].mean()
print("Average Price : ", avg_price)

max_price = df["price"].max()
print("Maximum Price : ", max_price)

min_price = df["price"].min()
print("Minimum Price : ", min_price)

df["price_change"] = df["price"] - df["price"].shift(1)

df["price_change_percentage"] = (df["price_change"]/df["price"].shift(1))*100
df["price_change_percentage"] = df["price_change_percentage"].round(3).astype(str) + "%"

print("\n", df.head())