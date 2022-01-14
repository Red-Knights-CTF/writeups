# Belarus

**Category**: OSINT \
**Points**: 20

## Description

> Find the nearest station to the place where this photo was taken:

Flag format:- SCTF{station_name_all_small_without_spaces}

![](que.png)
## Solution

Given file is 

![image.png](image.png).

Using reverse image lookup, I got the same image with good quality
![](image_good_quality.png).

By looking closer, I got a name `English National Ballet`.
![](image_zoom.png)

Searched it on google map and got this:
![](image_map.png)

The google map shows that the nearest train station is "Canning Town" which is the flag.
![](image_station.png)

# Flag is `SCTF{canningtown}`
 
