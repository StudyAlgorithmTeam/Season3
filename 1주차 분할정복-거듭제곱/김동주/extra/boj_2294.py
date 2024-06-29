# 동전 2

import bisect
import functools
import sys


N, K = map(int, sys.stdin.readline().split())
V = sorted(set(int(sys.stdin.readline()) for i in range(N)))
N = len(V)


@functools.cache
def solve(k: int) -> int:
    if k < 0:
        return sys.maxsize
    if k == 0:
        return 0
    hi = min(bisect.bisect(V, k), N-1) # k 이하인 가장 큰 가치의 코인 인덱스 번호
    min_coins = sys.maxsize
    for i in range(hi, -1, -1):
        coins = 1 + solve(k-V[i])
        if min_coins > coins:
            min_coins = coins
    return min_coins


sys.setrecursionlimit(int(1e6))
ans = solve(K)
print(ans if ans != sys.maxsize else -1)
