# 평범한 배낭

import sys


N, K = map(int, sys.stdin.readline().split())
W = [0] * N
V = [0] * N
for i in range(N):
    W[i], V[i] = map(int, sys.stdin.readline().split())


# dp[i][k]는 i번째 물품까지 살펴 보았을 때, 남은 용량 k일 때 얻을 수 있는 최대 가치.
#
# N = 1일 경우, i = 0 일 때, i-1 = -1번째...
# 즉, 자기 자신에게서 값을 가져옴으로서 생기는 문제를 해결하기 위해 N+1(한 칸 여분을 둠), K+1 크기로 설정.
dp = [[0] * (K+1) for i in range(N+1)]

for i in range(N):
    for k in range(K+1):
        dp[i][k] = max(
            dp[i-1][k],
            dp[i-1][k-W[i]] + V[i] if k-W[i] >= 0 else 0,
        )


print(max(dp[N-1]))
