# Target 3
**category: OSINT**  
**points: 452**

## Description
You will have recieved a clue after solving the Target 2 challenge. Use to clue to find out the second target.

## Solution
After getting the flag for the previous challenge, we are given a clue:
> Maybe going WAYBACK can help you out.

We are also given a python script as a clue to find the target.

Wayback here implies a wayback webpage. First, lets check the wayback of redjohn190989's twitter page at https://web.archive.org/web/20201129132030/https://twitter.com/RedJohn05844438. We can see his latest tweet:
> Critical op intel on reddit. Give it a look.

In one of the Instagram posts from the first challenge, there is a comment that says 'r/oddlysatisfying'. After searching the subreddit for redjohn190989, I found this [post](https://www.reddit.com/user/redjohn190989/comments/k3987y/serious_investigation/). Inside, there is a link to this [pastebin](https://pastebin.com/LBV5BvEN). Unfortunately it is password-protected.

Now, let's take a look at the python script given.
```python
import struct
import socket
import random

s = socket.socket()
port  = 1015
s.connect(('35.238.225.156',port))
print("This is a hint client only for finding the format of the date as a password for pastebin")
print("What number do you think corresponds to date here?")
packet = str(raw_input())
s.send(packet)
print(s.recv(80))
```

After running the script and guessing a few times, I got the date which is 190989, from redjohn190989's username. This is the output:
`'Not bad, use - as separator for the date DD-MM-YY'`

Then I enter 19-09-89 as the password, this is the content of the pastebin:
> Investigating here : 27.4698° S, 153.0251° E

After that I entered the coordinates to google maps. The address was 127-115 Queen St, Brisbane City QLD 4000, Australia. So, redjohn190989 was investigating the new health minister of Brisbane city. Then, after some googling, I got the name "yvette d'ath". Now we can submit this to the bot.

**FLAG:** `b00t2root{m@st3r_0f_0s1nt}`

