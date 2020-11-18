# Malicious File

**Category: Osint** \
**Points: 30**

## Desciption

We detected the following malicious file in our network, we weren’t able to find any issues with it, can you find something?

## Challenge

- Given malware hash
- Find The Flag

## Solution

We were give a text file:
1. [malware](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Malicious%20File/malware)

We were given a `SHA-256` hash `88b35a9365e5cd2b32c03832d2c8c02a41e3cead40e49af02cf74a73bfa0dc8d` of a file. As mentioned in discription, it is a malware. The first website that pops to mind thinking about malwares is https://virustotal.com 

Paste your hash in the `Search` tab

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Malicious%20File/virustotal.png)

Result let us know that file is not a malware but the `Community` tab have something for us

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Malicious%20File/community.png)

Someone has left a url `https://pastebin.com/QqhzEFjK`. Going there will give u a `base64` string `QUZGQ1RGe2ZvbGxvd190aGVfYnJlYWRjcnVtYnN9`, Decode it.

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Malicious%20File/base64.png)

FLAG - AFFCTF{follow_the_breadcrumbs}

