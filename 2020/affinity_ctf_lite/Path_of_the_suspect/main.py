import requests
import pprint
import json
import time

# https://www.opencellid.org/ajax/searchCell.php?mcc=260&mnc=3&lac=52911&cell_id=8961

url = 'https://www.opencellid.org/ajax/searchCell.php'

with open('src.json', 'r') as f:
    src = json.load(f)

locs = []

for cell in src:
    payload = {
        'mcc': cell['mcc'],
        'mnc': cell['mnc'],
        'lac': cell['lac'],
        'cell_id': cell['cid']
    }

    response = requests.request('GET', url, params=payload)
    print("Received loc: ", response.json())
    locs.append(response.json())
    time.sleep(5)

with open('locs1.json', 'w') as f:
    f.write(json.dumps(locs, indent=4))
