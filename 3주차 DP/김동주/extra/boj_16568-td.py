# 엔비스카의 영혼

import functools
import sys


N, a, b = map(int, input().split())


@functools.cache
def f(n: int, did_wait=False) -> int:
    if n < 0:
        return sys.maxsize
    if n == 0:
        return 0
    t = 0
    if not did_wait:
        t += 1
        n -= 1
    t += min(f(n-1, True)+1, f(n-a, False), f(n-b, False))
    return t


sys.setrecursionlimit(int(1e7))
print(f(N))
