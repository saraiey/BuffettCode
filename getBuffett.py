import time
import requests
import json
import pandas as pd

BC_API_ENDPOINT = "https://api.buffett-code.com/api/v3/bulk/quarter"
APIKEY='xz06rapLvG9yPr3g56Jev5g9DNAhJgCU1qi3PL1h'

TICKER="3246"
FROM='2018Q3'
TO='2019Q2'

def read_list():
    # IDリストの読み込み →グループID取得へ
    idsfile = "./ids.txt"
    ids = open(idsfile, "r")
    idslist = json.load(ids)
    ids.close
    return idslist

def fetch(ticker=None, start=None, end=None):
    if not ticker:
        print('Tickerを設置する')
        return
    if not start and not end:
        print('startとendの設定 例:2017Q1')
        return
    response = requests.get(
        url=BC_API_ENDPOINT,
        params={
            "ticker":ticker,
            "from":start,
            "to":end,
        },
        headers={
            "x-api-key":APIKEY,
        },
    )
    return response

idslist = read_list()
for i in idslist:
    res = fetch(idslist["ids"][i], FROM, TO)
time.sleep(3)
json_data = json.loads(res.text)
df = pd.DataFrame.from_dict(json_data['data']['2018Q3'])
df2 = pd.DataFrame.from_dict(json_data['data']['2018Q4'])
df3 = pd.DataFrame.from_dict(json_data['data']['2019Q1'])
df4 = pd.DataFrame.from_dict(json_data['data']['2019Q2'])
df = df2.append(df)
df = df3.append(df)
df = df4.append(df)
print(df)
df.to_csv("./data.csv")