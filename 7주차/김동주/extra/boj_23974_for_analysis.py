# 짝수 게임

from sys import setrecursionlimit
from functools import cache


@cache
def can_yg_win(yg: int, k: int) -> bool:
    if k == 0:
        return yg % 2 == 0
    for i in range(1, min(4, k)+1):
        if not can_hs_win((yg+i) % 2, k-i):
            return True
    return False

@cache
def can_hs_win(yg: int, k: int) -> bool:
    if k == 0:
        return yg % 2 == 1
    for i in range(1, min(4, k)+1):
        if not can_yg_win(yg, k-i):
            return True
    return False


if __name__ == "__main__":
    N, K = map(int, input().split())
    setrecursionlimit(K)
    print('YG' if can_yg_win(N, K) else 'HS')
