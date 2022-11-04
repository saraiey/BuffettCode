import json
import pandas_datareader as pdr
import datetime

# Ticker読み込む
def read_ticker():
    tickerfile = "./ticker.txt"
    tickers = open(tickerfile, "r")
    tickerslist = json.load(tickers)
    tickers.close
    return tickerslist

if __name__ == "__main__":
    tickerslist = read_ticker()
    stockTickerlist = [str(t)+'.JP' for t in tickerslist["ticker"]]
    startdate = datetime.date(2012,1,1)
    enddate = datetime.date.today()
    df = pdr.DataReader(stockTickerlist, 'stooq', startdate, enddate)
    print(len(df.index))
    stockData = df["Close"]
    stockData.to_csv("./stock_price_data.csv", encoding = "utf-8")