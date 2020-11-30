import json
import matplotlib.pyplot as plt

with open('src.json', 'r') as f:
    src = json.load(f)

with open('locs.json', 'r') as f:
    locs = json.load(f)

print(len(src))
print(len(locs))

groups = [5, 8, 7, 6, 4]
gi = 0
i = 0
while i < len(locs):
    group = locs[i: i + groups[gi]]
    lats = []
    lons = []
    for x in group:
        lats.append(x['lat'])
        lons.append(x['lon'])

    print(lats)
    print(lons)
    plt.plot(lons, lats, marker='o')

    i += groups[gi]
    gi += 1

# lats = []
# lons = []
# for loc in locs:
#     lats.append(loc['lat'])
#     lons.append(loc['lon'])

# plt.plot(lons, lats, marker='o')

plt.show()
