def G_Sum(n):
    if n < 0 :
        return 0
    return 1/(pow(2,n))+G_Sum(n-1)
    
print("KCTF{"+str(G_Sum(25))+"}")
