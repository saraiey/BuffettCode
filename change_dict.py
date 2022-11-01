import csv
dict_from_csv = {}
with open('company.csv', mode='r',encoding="utf-8") as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}
print(dict_from_csv)