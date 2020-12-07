# rasput1n's string
**category: programming**  
**points: 446**

## Description
Given an encrypted message, rasput1n encodes it the following way:

Removes the median letter of the word from the original word and appends it to the end of the encrypted word and repeats the process until there are no letters left.

A median letter in a word is the letter present in the middle of the word and if the word length is even, the median letter is the left one out of the two middle letters.

Can you decode the string?

## Solution
The mechanism of the encoding is already given in the question. We just need to reverse that.
Here's a python script to do that.

```python
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
```

**FLAG:** `b00t2root{@The_Director_is_the_bot}`
