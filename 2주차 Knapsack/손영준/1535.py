n = int(input()) #사람의 수
H = [0] + list(map(int, input().split())) #health
J = [0] + list(map(int, input().split())) #joyful
# list 1부터 시작.

#dp 테이블
dp = [[0]* 101 for _ in range(n+1)]

for x in range(1,n+1):
    h = H[x]
    j = J[x]
    for y in range(1,101):
        if y < h: #현재 사람 x
            dp[x][y] = dp[x-1][y]
        else: #현재 사람 o
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-h]+ j)

print(dp[n][99])
