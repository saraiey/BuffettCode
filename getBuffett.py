import requests
import json
import pandas as pd

#   API情報
BC_API_ENDPOINT="https://api.buffett-code.com/api/v3/quarter"
APIKEY='xz06rapLvG9yPr3g56Jev5g9DNAhJgCU1qi3PL1h'

# Ticker読み込む
def read_ticker():
    tickerfile = "./ticker.txt"
    tickers = open(tickerfile, "r")
    tickerslist = json.load(tickers)
    tickers.close
    return tickerslist

def read_fiscallist():
    fiscalfile = "./fiscal.txt"
    fiscals = open(fiscalfile, "r")
    fiscalslist = json.load(fiscals)
    fiscals.close
    return fiscalslist

def get_data(tickerslist, fiscalslist):
    df = pd.DataFrame()
    for ticker in tickerslist["ticker"]:
        for fy in fiscalslist["fiscal_year"]:
            for fq in ["1", "2", "3", "4"]:
                try:
                    response = requests.get(
                        url = BC_API_ENDPOINT,
                        params = {
                            "ticker":ticker,
                            "fy":fy,
                            "fq":fq
                        },
                        headers = {
                            "x-api-key":APIKEY
                        }
                    )
                    json_df = json.loads(response.text)
                    df1 = pd.DataFrame.from_dict(json_df['data'])
                    # df = df.append(df1)
                    df = pd.concat([df, df1])
                except Exception:
                    print(ticker + "の" + fy + "年第" + fq + "四半期のデータはありません。")
    return df

def create_data(df):
    data = df.loc["values"]
    return data

if __name__ == "__main__":
    tickerslist = read_ticker()
    fiscalslist = read_fiscallist()
    df = get_data(tickerslist, fiscalslist)
    data = create_data(df)
    data.to_csv("./data.csv")