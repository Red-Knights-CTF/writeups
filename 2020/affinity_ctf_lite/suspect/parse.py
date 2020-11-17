import pprint
import json


with open('src.txt', 'r') as f:
    fstr = f.read()

ss = fstr.splitlines()
locs = []
line_i = 0
while line_i < len(ss):
    print(ss[line_i])
    line_i += 1  # Registered at
    dates = ss[line_i].split()
    line_i += 1
    days = dates[0::2]
    times = dates[1::2]

    mccs = ss[line_i].split()
    line_i += 1
    mccs = mccs[1::2]
    mccs = [int(x) for x in mccs]

    mncs = ss[line_i].split()
    line_i += 1
    mncs = mncs[1::2]
    mncs = [int(x) for x in mncs]

    lacs = ss[line_i].split()
    line_i += 1
    lacs = lacs[1::2]
    lacs = [int(x) for x in lacs]

    cids = ss[line_i].split()
    line_i += 1
    cids = cids[1::2]
    cids = [int(x) for x in cids]

    rtypes = ss[line_i].split()
    line_i += 1
    rtypes = rtypes[2::3]

    for i in range(len(days)):
        loc = {}
        loc['day'] = days[i]
        loc['time'] = times[i]
        loc['mcc'] = mccs[i]
        loc['mnc'] = mncs[i]
        loc['lac'] = lacs[i]
        loc['cid'] = cids[i]
        loc['rtype'] = rtypes[i]
        locs.append(loc)

pprint.pprint(locs)

with open('src.json', 'w') as f:
    f.write(json.dumps(locs, indent=4))
