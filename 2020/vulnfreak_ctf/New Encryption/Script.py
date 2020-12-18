import hashlib
import string

with open('hash.txt') as f:
  fp = f.read()

md5_sum = ''

for j in range(0, len(fp), 40):
  tmp = fp[j:j+40]
  for i in '1234567890abcdef':
    letter  = hashlib.sha1(i.encode()).hexdigest()
    if letter == tmp:
      md5_sum += i
# print(md5_sum)

hsh = []
for j in range(0, len(fp), 32):
  hsh.append(md5_sum[j:j+32])

table = {}

for i in range(32, 127):
  tmp = chr(i)
  table[tmp] = hashlib.md5(tmp.encode()).hexdigest()

l = ''
for i in hsh:
  for j, k in table.items():
    if i == k:
      l += j
print(l)
