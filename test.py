import requests
import json
import pandas as pd

BC_API_ENDPOINT="https://api.buffett-code.com/api/v3/bulk/quarter"
APIKEY='xz06rapLvG9yPr3g56Jev5g9DNAhJgCU1qi3PL1h'

FROM='2018Q3'
TO='2019Q2'

idsfile = "./ids.txt"
ids = open(idsfile, "r")
idslist = json.load(ids)
ids.close

df = pd.DataFrame()

for id in idslist["ids"]:
    response = requests.get(
        url=BC_API_ENDPOINT,
        params={
            "ticker":id,
            "from":FROM,
            "to":TO,
        },
        headers={
            "x-api-key":APIKEY,
        },
    )
    json_df = json.loads(response.text)
    df1 = pd.DataFrame.from_dict(json_df['data']['2018Q3'])
    df = df.append(df1)
    df2 = pd.DataFrame.from_dict(json_df['data']['2018Q4'])
    df = df.append(df2) 
    df3 = pd.DataFrame.from_dict(json_df['data']['2019Q1'])
    df = df.append(df3)
    df4 = pd.DataFrame.from_dict(json_df['data']['2019Q2'])
    df = df.append(df4)

    print(df)

df.to_csv("./data.csv")