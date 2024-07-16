N=int(input())

l=list(map(int, input().split()))
t=sum(l)+8*(N-1)

print(t//24, t%24)
