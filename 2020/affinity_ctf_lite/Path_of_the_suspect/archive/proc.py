import json

with open('src.json', 'r') as f:
    src = json.load(f)

with open('locs.json', 'r') as f:
    locs = json.load(f)

print(len(src))
print(len(locs))

with open('mapcust.txt', 'w') as f:
    for loc in locs:
        f.write("{}, {}\n".format(loc['lat'], loc['lon']))
