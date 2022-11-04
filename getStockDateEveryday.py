import json
import pandas_datareader as pdr
import datetime
import schedule,time,datetime

def make_list():
# リストを読み込む
    tickerfile = "./ticker.txt"
    tickers = open(tickerfile, "r")
    tickerslist = json.load(tickers)
    tickers.close

# パラメータ作成
    stockTickerlist = [str(t)+'.JP' for t in tickerslist["ticker"]]
    startdate = datetime.date(2012,1,1)
    enddate = datetime.date.today()
    df = pdr.DataReader(stockTickerlist, 'stooq', startdate, enddate)
    print(len(df.index))
    stockData = df["Close"]
    stockData.to_csv("./stock_price_data.csv", encoding = "utf-8")

# 毎日10:00に実行
schedule.every().day.at("10:00").do(make_list)

while True:
    schedule.run_pending()
    time.sleep(1)