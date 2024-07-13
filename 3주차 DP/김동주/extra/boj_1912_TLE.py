# 연속합


from functools import cache

N = int(input())
A = [*map(int, input().split())]


@cache
def prefix_sum(i: int) -> int:
    if i < 0:
        return 0
    return prefix_sum(i-1) + A[i]


def range_sum(s: int, e: int) -> int:
    return prefix_sum(e) - prefix_sum(s-1)


def max_range_sum(s: int, e: int) -> int:
    max_sum = range_sum(s, s)
    for i in range(s, e+1):
        for j in range(i, e+1):
            max_sum = max(max_sum, range_sum(i, j))
    return max_sum


print(max_range_sum(0, N-1))
