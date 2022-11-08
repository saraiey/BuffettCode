import json
import pandas 
import pandas_datareader.data as web
import datetime

# Ticker読み込む
def read_ticker():
    tickerfile = "./test.txt"
    tickers = open(tickerfile, "r")
    tickerslist = json.load(tickers)
    tickers.close
    return tickerslist

if __name__ == "__main__":
    tickerslist = read_ticker()
    startdate = datetime.date(2012,1,1)
    enddate = datetime.date.today()
    df = []
    for t in tickerslist["ticker"]:
        ticker_symbol = [str(t)+'.JP']
        df1 = web.DataReader(ticker_symbol, data_source='stooq', start=startdate, end=enddate)
        df1 = df1.insert(0, "code", ticker_symbol, allow_duplicates=False)
        df = df.append(df1)
    print(len(df.index))
    # stockData = df["Close"]
    stockData = pandas.melt(df)
    stockData.to_csv("./stock_price_data.csv", encoding = "utf-8")