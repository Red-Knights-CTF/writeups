import json
import matplotlib.pyplot as plt

with open('locs.json', 'r') as f:
    locs = json.load(f)

with open('mapconv', 'w') as f:
    for loc in locs:
        f.write("{},{}\n".format(loc['lat'], loc['lon']))
