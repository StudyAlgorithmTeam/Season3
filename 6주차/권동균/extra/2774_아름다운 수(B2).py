T=int(input())
for i in range(T):
    l=[0]*10
    X=int(input())
    a=list(map(int, str(X)))
    for j in a:
        if l[j]==0:
            l[j]+=1
        else: continue
    print(sum(l))
