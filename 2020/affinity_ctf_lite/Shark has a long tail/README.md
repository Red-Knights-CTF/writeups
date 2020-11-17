# Shark has a long tail

**Category: Misc** \
**Points: 663**

## Desciption

We intercept the attack traffic and we know that there is a message in packets encoded in some tricky way. Can you help us decode it.

## Challenge

- Given SharkHasALongTail.pcap
- Find The Flag

## Solution

We were give a pcap file:
1. [SharkHasALongTail.pcap](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Shark%20has%20a%20long%20tail/SharkHasALongTail.pcap)

As all of us would do, i opened that pcap file in ```Wireshark```.

I literally tried everything, everything was normall. 

Then i saw something interesting.

The ```TCP``` header length of every packet was under ```255``` which means it could be decimal
![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Shark%20has%20a%20long%20tail/wire_shark.png)

Reading the documentation of ```tshark``` wireshark command line utility

I lead to this ```tshark -r SharkHasALongTail.pcap -T fields -e tcp.len```

It gives ```TCP``` header length of all packets

Copy all that numbers and paste them into ```CyberChecf``` \
[tcp_lengths.txt](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Shark%20has%20a%20long%20tail/tcp_lengths.txt)

Use ```From Decimal``` Recipe 

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Shark%20has%20a%20long%20tail/CyberChef.png)

FLAG - ```AFFCTF{TCPDUMP_Never_Disappoints}```

