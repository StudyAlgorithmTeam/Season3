N=int(input())
M=int(input())
S=input()

P=[0]*N
cnt=0
P[0]='IOI'
cnt=0
P_n='IO'*N+'I'
i=0

while i<(M-1):
    if S[i]=='I':
        if S[i:i+len(P_n)]==P_n:
            cnt+=1
        else:
            continue
    else:
        continue
print(cnt)
