N = int(input())
S = input().strip()


dp = [0] * N


for i in reversed(range(N)):
    can_start_sing = True
    for j in range(i, N):
        if S[j] != S[j-i]:
            can_start_sing = False
            break

    if not can_start_sing:
        continue

    for j in range(i, N):
        if dp[i] > dp[j]+1:
            continue

        for k in range(N, i+N):
            if S[k-j] != S[k-i]:
                break
        else:
            dp[i] = dp[j] + 1


print(max(dp))