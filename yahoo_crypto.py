import pandas as pd
import yfinance as yf

ticker = ["BTC-GBP", "ETH-USD"]

crypto = yf.download(ticker, period="5y")
print(crypto)