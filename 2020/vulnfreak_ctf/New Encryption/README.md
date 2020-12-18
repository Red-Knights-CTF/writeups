# New Encryption

It was a Crypto-200 chall in the Hackfest0x01 CTF

In this chall we got two files **encrypt.py** and **hash.txt**

The hash.txt file contains some sort of hash.

The encrypt.py file is a python script having the contents

```
import hashlib

flag = "**REDACTED**"
result = ""
md5_cipher=""

for element in flag:
  element  = hashlib.md5(element.encode())
  element  = element .hexdigest()
  md5_cipher +=str(element )

for letter in md5_cipher:
 
  letter  = hashlib.sha1(letter .encode())
  letter  = letter .hexdigest()
  result += str(letter )

f = open('hash.txt','w')
f.write(result)
f.close()
```

## Recon

Its super short script used to encrypt the flag. Lets go through the code 

1. First it import hashlib module and initializes some variables, and stores the flag into *flag* varible.

```
import hashlib

flag = "**REDACTED**"
result = ""
md5_cipher=""
```

2. Then for each character of flag, it calculates md5sum of that char then does a hexdigest on it and finally appends it to md5_cipher.

```
for element in flag:
  element  = hashlib.md5(element.encode())
  element  = element .hexdigest()
  md5_cipher +=str(element )
```


3. Again for every character in md5_cipher, it calculates sha1 of char then does a hexdigest on it and then appends it to the result variable.

```
for letter in md5_cipher:
 
  letter  = hashlib.sha1(letter .encode())
  letter  = letter .hexdigest()
  result += str(letter )
```

4. Finally we saves the result in the **hash.txt** file.

```
f = open('hash.txt','w')
f.write(result)
f.close()
```

Since it is calculating hashes char-by-char, it is easily bruteforcable

We just have to do these operations in reverse order, i.e. first break the sha1hash and then break the md5 hash


## Solution

Lets implement the algo step by step

1. I open the hash.txt and stored the contents into the fp variable, and also imported some modules which will be required

```
import hashlib

with open('hash.txt') as f:
  fp = f.read()

md5_sum = ''
```

2. Remembered that it is calculating sha1 hash from **hexdigest** of md5 hash, therefore the possibility of characters is just 16(all the hex characters) which is easily bruteforcable. Also the length of sha1 hash in **hex** is 40 so we have to take 40 characters at a time from the fp

```
for j in range(0, len(fp), 40):
  tmp = fp[j:j+40]               # Dividing the hash into chunks of length 40
  for i in '1234567890abcdef':   # Possible chars
    letter  = hashlib.sha1(i.encode()).hexdigest() # calculating sha1 hash
    if letter == tmp:            # checking the sum 
      md5_sum += i
```

3. Now we have the md5sum, we can do the same to get the plaintext back. I precomputed the hash values of all the printable characters into a dictionary and then cheking it with our hash

```
hsh = []
for j in range(0, len(fp), 32):  # hex length of md5sum - 32
  hsh.append(md5_sum[j:j+32])

table = {}

for i in range(32, 127):
  tmp = chr(i)
  table[tmp] = hashlib.md5(tmp.encode()).hexdigest() # Precomputing the hash values

o = ''
for i in hsh:
  for j, k in table.items():
    if i == k:               # Checking for similar hash
      o += j                 # Appending into output varible
print(o)                     # Printing the output
```

Running the script gives the flag
```
N0w_y0u_4r3_r3ady_f0r_7h3_3ncryp710n_j0urn3y_may_y0u_3nj0y3d_I7
```

Whole script can be found [here](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/vulnfreak_ctf/New%20Encryption/Script.py)
