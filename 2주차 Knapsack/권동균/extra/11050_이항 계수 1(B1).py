def fact(x):
    t=1
    for i in range(1, x+1):
        t*=i
    return t

def bc(x,y):
    return int(fact(x)/(fact(y)*fact(x-y)))

N,K=map(int, input().split())

print(bc(N,K))
