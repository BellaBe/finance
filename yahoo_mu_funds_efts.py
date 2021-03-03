import pandas as pd
import yfinance as yf

ticker = "TLT" #iShares 20+ Year Treasury Bond ETF
ticker2="OMOIX" #Vivaldi Multi-Strategy Fund C:ass I

tlt = yf.download(ticker, period = "5y")
omoix = yf.download(ticker2, period = "5y")

print(tlt)
print(omoix)