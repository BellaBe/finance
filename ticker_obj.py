import pandas as pd
import yfinance as yf

ticker = "DIS"
dis = yf.Ticker(ticker)
# print(dis)
# print(dis.ticker)
# print(dis.history())
# print(dis.info)
# print(pd.Series(dis.info))
# pd.Series(dis.info)

df = pd.Series(dis.info, name="DIS").to_frame().T
#print(df)

tickers = ["MSFT", "FB"]
# for i in tickers:
#     df.loc["{}".format(i)] = pd.Series(yf.Ticker(i).info)

# print(df)

# print(dis.balance_sheet)
# print(dis.financials)
# print(dis.cashflow)


# tickerG = ["AAPL", "FB", "AMZN"]

# for i in tickerG:
#     yf.Ticker(i).financials.to_csv("{}.csv".format(i))

calls = dis.option_chain()[0]
print(calls)
puts = dis.option_chain()[1]
print(puts)