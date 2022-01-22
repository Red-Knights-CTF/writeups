import math

a = 21525625
b = 30135875

def DigitSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

answer = DigitSum(math.gcd(a, b)) * 1234
print("KCTF{"+str(answer)+"}")
