import pandas as pd
import yfinance as yf

ticker = ["DJI", "^GSPC"]

indexes = yf.download(ticker, period="5y").Close
indexes_head = yf.download(ticker, period="5y")
norm = indexes.div(indexes.iloc[0]).mul(100)


print(indexes)

print(indexes_head.head())
print(norm)
#print(norm.plot())