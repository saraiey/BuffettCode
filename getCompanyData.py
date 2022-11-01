import requests
import json
import pandas as pd

#   API情報
BC_API_ENDPOINT="https://api.buffett-code.com/api/v3/company"
APIKEY='xz06rapLvG9yPr3g56Jev5g9DNAhJgCU1qi3PL1h'

# Ticker読み込む
def read_ticker():
    tickerfile = "./ticker.txt"
    tickers = open(tickerfile, "r")
    tickerslist = json.load(tickers)
    tickers.close
    return tickerslist

def get_data(tickerslist):
    df = pd.DataFrame()
    for ticker in tickerslist["ticker"]:
        try:
            response = requests.get(
                url = BC_API_ENDPOINT,
                params = {
                    "ticker":ticker,
                },
                headers = {
                    "x-api-key":APIKEY
                }
            )
            json_df = json.loads(response.text)
            df1 = pd.DataFrame.from_dict(json_df['data'])
            df = pd.concat([df, df1])
        except Exception:
            print(ticker + "のデータはありません。")
    return df

if __name__ == "__main__":
    tickerslist = read_ticker()
    df = get_data(tickerslist)
    df.to_csv("./companydata.csv")