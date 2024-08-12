# 돌 게임 7

import functools


@functools.cache
def can_win(N: int) -> bool:
    x = 1
    while x <= N:
        if not can_win(N-x):
            return True
        x *= 4
    return False


def analysis():
    N = 100
    # S[N]: 돌이 N개 있을 때, 상근이가 이기면 'O', 지면 'X'
    S = ['SK' if can_win(n) else 'CY' for n in range(1, N+1)]
    # find smallest repeating substring
    for n in range(1, N+1):
        if all(S[:n] == S[offset:offset+n] for offset in range(n, N+1, n) if offset+n <= N):
            return S[:n]
    raise ValueError


# PATTERN = analysis()
PATTERN = ['SK', 'CY', 'SK', 'SK', 'CY']

N = int(input())
print(PATTERN[(N-1) % len(PATTERN)])