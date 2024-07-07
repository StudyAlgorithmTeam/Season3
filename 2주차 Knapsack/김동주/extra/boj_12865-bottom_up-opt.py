# 평범한 배낭

import sys


N, K = map(int, sys.stdin.readline().split())
W = [0] * N
V = [0] * N
for i in range(N):
    W[i], V[i] = map(int, sys.stdin.readline().split())


# dp[k]는 i번째 iteration에서 i번째 물품까지 살펴 보았을 때 기준
# k의 용량으로 얻을 수 있는 최대 가치.
dp = [0] * (K+1)
for i in range(N):
    for k in range(K, W[i]-1, -1):
        dp[k] = max(
            dp[k],
            dp[k-W[i]] + V[i],
        )


print(dp[K])
