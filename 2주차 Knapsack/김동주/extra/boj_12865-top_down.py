# 평범한 배낭

from functools import cache
import sys


N, K = map(int, sys.stdin.readline().split())
W = [0] * N
V = [0] * N
for i in range(N):
    W[i], V[i] = map(int, sys.stdin.readline().split())


@cache
def knapsack(i: int = 0, k: int = K) -> int:
    if k < 0:
        return -sys.maxsize
    if i == N:
        return 0
    return max(
        knapsack(i+1, k),
        knapsack(i+1, k-W[i]) + V[i],
    )

print(knapsack())
