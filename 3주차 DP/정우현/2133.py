N = int(input())
dp = [0]*31

dp[2] = 3
dp[4] = 11

def tile(N):
    if N%2 == 1:
        dp[N] = 0
    else:
        dp[N] = dp[N-2]*dp[2]
        for j in range(2,N-2,2):
            dp[N] += dp[j]*2
        dp[N] += 2


if N < 6:
    print(dp[N])
else:
    for i in range(6,N+1,2):
        tile(i)
        
    print(dp[N])