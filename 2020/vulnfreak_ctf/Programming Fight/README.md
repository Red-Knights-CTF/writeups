# Programming Fight

*Hint : Next File Name Matters a Lot*

Programming Fight was a Crypto challenge in the Hackfest0x01 CTF.

According to me it was not a crypto challenge at all, it should be either Programming or Misc challenge.

In the challenge we get a zip file **1300.zip**, it was password protected and inside that was another zip file **1299.zip**

So the problem is simple, it is like a Matryoshka, zip inside a zip inside a zip ...,
but the problem is that they are all password protected. But as the hint says *Next File Name Matters a Lot*, I tried using the Next filename as a password, but it didnt work.

Another point to be noted is that in the description this was mentioned **digest our password five times**, so maybe the password is md5 of the next file, and indeed it was. So now the problem is simple we just have to do all this in a loop till **0.zip** file is left

I wrote a shot python script which just does all this

```
import hashlib
import subprocess

for i in range(1300, 0, -1):
  fname = str(i) + '.zip'                                  # Generating the filename to be extracted
  next_file = str(i-1).encode()                            # Next filename which is 1 less the previous one
  passwd = hashlib.md5(next_file).hexdigest()              # Calculating md5sum
  d = subprocess.getoutput(f'unzip -P "{passwd}" {fname}') # Using the unzip command
  print(f'\r{fname}')                                      # Printing the current filename
  subprocess.getoutput(f'del {fname}')                     # Deleting the file which is no longer needed
```

After running this script we are left with **0.zip** which is again password protected but this time the password is **flag**

Extracting that gives us our flag

```
hf0x01{T7h1$_sh0w$_Y0u_Kn0w_pr0gr4mm1nG_4nD_ha$1nG_v3rY_W3LL}
```
