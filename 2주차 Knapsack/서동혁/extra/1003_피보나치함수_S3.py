T = int(input())

fibo = {0:(1,0), 1:(0,1)}

def dp(n):
    if n not in fibo:
        fibo[n] = (dp(n-1)[0]+dp(n-2)[0], dp(n-1)[1]+dp(n-2)[1])

    return fibo[n]
    
    

for i in range(T):
    N = int(input())

    a,b = dp(N)
    print(a,b)