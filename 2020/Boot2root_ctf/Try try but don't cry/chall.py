import random
def xor(a,b):
	l=""
	for i in range(min(len(a), len(b))):
		l+=chr(ord(a[i]) ^ ord(b[i]))
	return l

def encrypt(flag):
	l=random.randrange(2)
	if(l==0):
		return flag.encode('base64')
	elif(l==1):
		return flag.encode('hex')
	

flag="################"
assert(len(flag)==22)
c=xor(flag[:11], flag[11:])
c=c.encode('hex')

n=random.randint(1,20)
#print(n)

for _ in range(n):
	c=encrypt(c)

f=open('chall.txt', 'w')
f.write(c)
f.close()



