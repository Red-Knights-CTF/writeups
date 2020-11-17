# sooodefault

**Category**: Web \
**Points**: 30

opening the given link. `http://web2.affinityctf.com/`
it's give us a Apache2 Ubuntu Default Page. 
If we compare the page with any Apache2 Default page, will notice there a html entites, if you decoding this it's will give us the flag but i'm wrote a fast script for collect and decode :D 
```import requests
import re
r=requests.session()
url="http://web2.affinityctf.com/"
op=r.get(url)
op=re.findall("&#[0-9]{2,3}",op.text)
print(op)
print(''.join([chr(int(i.replace("&#",""))) for i in op]))
```
![](/assets/injector/script.png)

The flag is `AFFCTF{htmlentity}`
