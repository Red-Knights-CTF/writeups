import re

with open('file', 'r') as f:
    str1 = f.read()

n = len(str1)
me = (n + 1) // 2

result = [''] * n
result[me - 1] = str1[0]
str1 = str1[1:]

j = me - 2
for i in range(0, n - 1, 2):
    result[j] = str1[i]
    j -= 1
    
j = me
for i in range(1, n - 1, 2):
    result[j] = str1[i]
    j += 1

str2 = ''.join(result)
flag = re.findall('b00t2root{.*}', str2)[0]
print(flag)
