T=int(input())

for i in range(T):
    l=list(map(int, input().split()))
    HP=l[0]+l[4]
    MP=l[1]+l[5]
    atk=l[2]+l[6]
    dfs=l[3]+l[7]

    if HP<1: HP=1
    if MP<1: MP=1
    if atk<0: atk=0
    result=1*HP+5*MP+2*atk+2*dfs
    print(result)

