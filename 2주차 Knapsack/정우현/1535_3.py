N = int(input())  # 사람의 수

L = list(map(int, input().split()))  # 각 사람마다 잃는 체력
J = list(map(int, input().split()))  # 각 사람마다 얻는 기쁨

dp = [[0] * 100 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(100):
        # 현재 사람을 선택하지 않는 경우
        dp[i][j] = dp[i - 1][j]
        # 현재 사람을 선택하는 경우 : 체력이 넘지 않는지 확인
        if j >= L[i - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - L[i - 1]] + J[i - 1])

print(dp[N][99])
