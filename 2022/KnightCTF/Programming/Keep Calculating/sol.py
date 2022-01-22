x=1
y=x+1
xy=12
answer=0
for i in range(666):
    answer += (x*y) + int(str(x)+str(y))   
    x+=1 
print("KCTF{"+str(answer)+"}")        
