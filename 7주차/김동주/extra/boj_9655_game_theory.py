# 돌 게임

import functools


@functools.cache
def can_win(N: int) -> bool:
    # O(N)
    if N >= 3 and not can_win(N-3):
        return True
    if N >= 1 and not can_win(N-1):
        return True
    return False


N = int(input())
print('SK' if can_win(N) else 'CY')

# 혹은
# print('SK' if N % 2 else 'CY')
