x=1
answer = 0

for i in range(543):
    calculation = (x*(x+1)) + (2 *(x + 1))
    reversed_calc = int(str(calculation)[::-1])
    if reversed_calc % 4 == 0:
        answer=answer+reversed_calc
    x+=1    

print("KCTF{"+str(answer)+"}")
