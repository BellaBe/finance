import pandas as pd 
import yfinance as yf 
import matplotlib.pyplot as plt

################################################################
#ticker = "GE"
#GE = yf.download(ticker, start="2014-01-01", end="2018-12-31")
# print(GE.head())
# print(GE.tail())
# print(GE)
# print(GE.info())
# GE_max = yf.download(ticker, period="max")
# print(GE_max)
# GE_ytd = yf.download(ticker, period="ytd")
# print(GE_ytd)
# GE_10y = yf.download(ticker, period="10y")
# print(GE_10y)
# GE_5y = yf.download(ticker, period="5y")
# print(GE_5y)
# GE_2y = yf.download(ticker, period="2y")
# print(GE_2y)
# GE_1y = yf.download(ticker, period="1y")
# print(GE_1y)
# GE_6mo = yf.download(ticker, period="6mo")
# print(GE_6mo)
# GE_3mo = yf.download(ticker, period="3mo")
# print(GE_3mo)
# GE_1mo = yf.download(ticker, period="1mo")
# print(GE_1mo)
# GE_5d = yf.download(ticker, period="5d")
# print(GE_5d)
# GE_1d = yf.download(ticker, period="1d", prepost=True, interval="1h")
# print(GE_1d)
# GE_1d = yf.download(ticker, period="1d", interval="5m")
# GE_1d = yf.download(ticker, period="1d", interval="5m")
# print(GE_1d.head(10))
# print(GE_1d.describe())
################################################################

# ticker = "AAPL"
# AAPL = yf.download(ticker, period="10y", actions=True)
# AAPL.to_csv("AAPL.csv")
# pd.read_csv("AAPL.csv", parse_dates=["Date"], index_col="Date")
# AAPL.to_excel("AAPL.xls")
# pd.read_excel("AAPL.xls", parse_dates=["Date"], index_col="Date")
# #print(AAPL)
# dividends = AAPL[AAPL["Dividends"] > 0]
# print(dividends)

# print(AAPL.loc["2019-08-05":"2019-08-15"])
# print(AAPL.loc["2019-08-05":"2019-08-15"].diff())

# stock_split = AAPL[AAPL["Stock Splits"] > 0]
# print(stock_split)

################################################################
#%%%
import pandas as pd 
import yfinance as yf 
#import matplotlib.pyplot as plt
tickers = ["AAPL", "FB", "GE"]

#stocks = yf.download(tickers, period="5y", group_by="Ticker")
stocks = yf.download(tickers, period="5y").Close
print(stocks)
print(stocks.head())
#stocks.plot()
#plt.show()
# %%
