import pandas as pd
import yfinance as yf

ticker1 = "^TNX"
ticker2 = "^FVX"

ticker = [ticker1, ticker2]

data = yf.download(ticker, period="5y").Close
print(data)