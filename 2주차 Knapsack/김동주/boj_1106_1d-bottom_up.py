# 호텔

import sys


MAX_C = 1000
MAX_ARG = 100

C, N = map(int, sys.stdin.readline().split())
group_cost = [None] * N
group_size = [None] * N
for i in range(N):
    group_cost[i], group_size[i] = map(int, sys.stdin.readline().split())

# Bottom-up DP
COST = [sys.maxsize] * (MAX_C+1 + MAX_ARG)
COST[0] = 0
for c in range(C):
    for i in range(N):
        alt_c = c + group_size[i]
        COST[alt_c] = min(COST[alt_c], COST[c] + group_cost[i])

print(min(COST[C:]))
