N=int(input())

R=[]
G=[]
B=[]

for i in range(N):
    r,g,b=map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

for i in range(1, N):
    R[i]+=min(G[i-1], B[i-1])
    G[i]+=min(R[i-1], B[i-1])
    B[i]+=min(R[i-1], G[i-1])
    
print(min(R[-1],G[-1],B[-1]))
