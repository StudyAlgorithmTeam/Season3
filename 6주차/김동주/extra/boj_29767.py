# 점수를 최대로

N, K = map(int, input().split())
A = [*map(int, input().split())]

# O(N) for prefix sum
prefix_sum = [0] * N
for i in range(N):
    prefix_sum[i] = prefix_sum[i-1] + A[i]

# O(N log N) for sorting
greedy = sorted([*range(N)], key=lambda i: -prefix_sum[i])

# O(K) for greedy approach
answer = 0
for i in greedy[:K]:
    answer += prefix_sum[i]

print(answer)
