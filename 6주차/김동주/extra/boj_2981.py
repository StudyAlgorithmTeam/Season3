# 검문

import sys


N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readlines())] # O(N)


def is_valid(mod: int) -> bool:
    # O(N)
    m = A[0] % mod
    for a in A:
        if a % mod != m:
            return False
    return True


# O(N * max(A))
print(*filter(is_valid, range(2, max(A)+1)))
