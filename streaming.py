import pandas as pd 
import yfinance as yf 
import time 

while True:
    time.sleep(60)
    data = yf.download("EURUSD=X", interval ="1m", period="1d")
    print(data.index[-1], data.iloc[-1,3])
