def sumSquare(n) :
    ans = []
    c = 0
    i = 1
    while i * i <= n :
        j = 1
        while(j * j <= n) :
            if (i * i + j * j == n) :
                print(i, "^2 + ", j , "^2" )
                c += 1
                if c == 3:
                    ans.append(str(i))
                    ans.append(str(j))
            j = j + 1
        i = i + 1
    return ans    
n = 25000
num = sumSquare(n)
print("\n\nKCTF{"+num[0]+","+num[1]+"}")
