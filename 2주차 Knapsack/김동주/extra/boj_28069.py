N, K = map(int, input().split())

# K번 이내에만 도달하면 된다.
# K번보다 더 적은 횟수 L에 도달하는 경우에는
# 시작 위치 0에서 K-L번 i+i/2로 이동.
# 즉, 제자리에서 있으면 된다.

dp = [None] * (2*N+1) # dp[i]: i번째 위치에 도달할 때까지 필요한 최소 이동 횟수
dp[0] = 0

for i in range(N):
    if dp[i] is None:
        continue
    if dp[i+1] is None:
        dp[i+1] = dp[i] + 1
    if dp[i+i//2] is None:
        dp[i+i//2] = dp[i] + 1

if dp[N] is not None and dp[N] <= K:
    print('minigimbob')
else:
    print('water')
