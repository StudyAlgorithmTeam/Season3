n = int(input()) # 사람 수
L = list(map(int, input().split())) # 체력 잃기
J = list(map(int, input().split())) # 기쁨 얻기

# HP
dp=[0]*100

# HP 99부터 쫙 내려가면서 모든 경우의 수 구하기
for i in range(n):
    for j in range(99, L[i]-1,-1):
        dp[j]=max(dp[j], dp[j-L[i]]+J[i])

print((dp))
