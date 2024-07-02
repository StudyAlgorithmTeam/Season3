# 수들의 합 4


N, K = map(int, input().split())
A = [*map(int, input().split())]

# prefix sum
prefix_sum = [*A]
for i in range(1, N):
    prefix_sum[i] += prefix_sum[i-1]

cases = 0
for j in range(N):
    for i in range(j+1):
        sub_sum = prefix_sum[j] - prefix_sum[i] + A[i]
        if sub_sum == K:
            cases += 1

print(cases)
