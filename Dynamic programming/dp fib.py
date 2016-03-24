



N     = 10**5
L     = [-1]*(N+1)
L[0] , L[1] = 0,1


def fib(n):
    global L
    if L[n]  == -1:
        L[n] = (fib(n-1))**2 + fib(n-2)
    return L[n]
    
    
print fib(N)




