import requests
import pprint
import json

url = "https://us1.unwiredlabs.com/v2/process.php"
token = "pk.62bce8462ad93af8bb529310a573e935"

# payload = {
#     "token": "pk.62bce8462ad93af8bb529310a573e935",
#     "radio": "gsm",
#     "mcc": 260,
#     "mnc": 3,
#     "cells": [{
#         "lac": 52911,
#         "cid": 8961
#     }],
#     "address": 1
# }

with open('src.json', 'r') as f:
    src = json.load(f)

locs = []

for cell in src:
    payload = {
        'token': token,
        'radio': cell['rtype'],
        'mcc': cell['mcc'],
        'mnc': cell['mnc'],
        'cells': [{
            'lac': cell['lac'],
            'cid': cell['cid']
        }],
        'address': 1
    }

    response = requests.request('POST', url, json=payload)
    print("Received loc")
    locs.append(response.json())

with open('locs.json', 'w') as f:
    f.write(json.dumps(locs, indent=4))
