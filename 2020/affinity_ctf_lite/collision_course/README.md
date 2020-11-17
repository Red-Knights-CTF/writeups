# Collision course

**Category**: Cryptography \
**Points**: 500

## Challenge
- Create 2 DIFFERENT files with the same md5 hash.
- Additionally, the files have to contain the phrase: "AFFCTF".
- File size limit is is 100000b

## Solution

Grab two 4.0KB example files with an md5 collision:
1. [collision1.zip](https://github.com/corkami/collisions/blob/master/examples/collision1.zip)
2. [collision2.zip](https://github.com/corkami/collisions/blob/master/examples/collision2.zip)

Append `AFFCTF` to both.
```
$ md5sum collision1.zip collision2.zip
2b980a3708ff9edfdd6c8dfbb42e4f8d  collision1.zip
2b980a3708ff9edfdd6c8dfbb42e4f8d  collision2.zip

$ echo "AFFCTF" >> collision1.zip
$ echo "AFFCTF" >> collision2.zip

$ md5sum collision1.zip collision2.zip
f6ff7f5a9c9dfcb3715d05bde1e6f708  collision1.zip
f6ff7f5a9c9dfcb3715d05bde1e6f708  collision2.zip
```

Submitting this to the challenge page, I got:
```
Checking, please wait...
String found in the first file
String found in the second file
Checking if files are different...
Files are different
Checking if files are MD5 Hash is the same for both files...
MD5Hashes are the same. You were right. The flag is: AFFCTF{One_Way_Or_Another}
```
