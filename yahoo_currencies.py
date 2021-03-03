import pandas as pd
import yfinance as yf

ticker = "EURUSD=X"
ticker2 = "USDEUR=X"
ticker3 = "USDGBP=X"
eurusd = yf.download(ticker, perdiod="1d")
usdeur = yf.download(ticker2, perdiod="1d")
usdgbp = yf.download(ticker3, perdiod="1d")
print(eurusd)
print(usdeur)
print(usdgbp)