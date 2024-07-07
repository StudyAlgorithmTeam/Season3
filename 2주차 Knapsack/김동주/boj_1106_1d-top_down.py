# 호텔

import sys


MAX_C = 1000

C, N = map(int, sys.stdin.readline().split())
group_cost = [None] * N
group_size = [None] * N
for i in range(N):
    group_cost[i], group_size[i] = map(int, sys.stdin.readline().split())


def cache_via_list(func):
    CACHE = [None] * (2*MAX_C+1)  # -C ~ C 범위를 커버

    def wrapper(c):
        nonlocal CACHE
        if CACHE[c] is None:
            CACHE[c] = func(c)
        return CACHE[c]
    return wrapper


@cache_via_list
def find_min_price(c: int) -> int:
    """c명의 고객을 유치하기 위해 투자해야할 최소 금액"""
    if c <= 0:
        return 0
    return min(
        find_min_price(c - group_size[i]) + group_cost[i]
        for i in range(N)
    )


sys.setrecursionlimit(10 * C)
print(find_min_price(C))
