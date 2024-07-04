# 호텔

import sys


MAX_C = 1000
CACHE = [None] * (MAX_C+1)


C, N = map(int, sys.stdin.readline().split())
unit_price = [None] * N
unit_amount = [None] * N
for i in range(N):
    unit_price[i], unit_amount[i] = map(int, sys.stdin.readline().split())


def find_min_price(c = C) -> int:
    """c명의 고객을 유치하기 위해 투자해야할 최소 금액"""
    if c <= 0:
        return 0
    if CACHE[c] is None:
        CACHE[c] = min(find_min_price(c - unit_amount[i]) + unit_price[i] for i in range(N))
    return CACHE[c]


sys.setrecursionlimit(10 * MAX_C)
print(find_min_price())
