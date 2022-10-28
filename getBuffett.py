import requests
import json
import pandas as pd

BC_API_ENDPOINT = "https://api.buffett-code.com/api/v3/quarter"
APIKEY='xz06rapLvG9yPr3g56Jev5g9DNAhJgCU1qi3PL1h'

TICKER="3246"
fy='2018'
fg='3'

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
            "fy":start,
            "fq":end,
        },
        headers={
            "x-api-key":APIKEY,
        },
    )
    return response

res = fetch(TICKER, fy, fg)
json_data = json.loads(res.text)
df = pd.DataFrame.from_dict(json_data['data'])
print(df)