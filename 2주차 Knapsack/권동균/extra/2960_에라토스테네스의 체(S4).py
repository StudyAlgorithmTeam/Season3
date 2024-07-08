N, K = map(int, input().split())
# N : 마지막 수
# K : k번째 지우는 수

l=[]
c=[0]*(N-1)
s=[]

# 2~N까지의 범위 리스트 생성
for i in range(2, N+1):
    l.append(i)

for i in range(2,N+1):
    for j in l:
        if(j%i==0):
            if(j in s): continue
            else: s.append(j)
print(s[K-1])
