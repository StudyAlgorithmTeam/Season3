# 절망적인 줄

import sys


MOD = 1000000
MAX_N = 1000

CACHE = [[None] * (MAX_N//2 + 1) for _ in range((MAX_N//2 + 1))]
N: int
HALF_N: int
STRING: str


def solve(coin50: int = 0, coin100: int = 0) -> int:
    if (coin50 > HALF_N) or (coin100 > HALF_N) or (coin50 < coin100):
        return 0
    if (coin50 == HALF_N) and (coin100 == HALF_N):
        return 1
    if CACHE[coin50][coin100] is None:
        i = coin50 + coin100
        if STRING[i] == '(':
            CACHE[coin50][coin100] = solve(coin50+1, coin100)
        elif STRING[i] == ')':
            CACHE[coin50][coin100] = solve(coin50, coin100+1)
        else:
            CACHE[coin50][coin100] = (solve(coin50+1, coin100) + solve(coin50, coin100+1)) % MOD
    return CACHE[coin50][coin100]


def clear(s: str):
    global STRING, N, HALF_N
    STRING = s
    N = len(s)
    HALF_N = N//2
    for coin50 in range(HALF_N+1):
        for coin100 in range(HALF_N+1):
            CACHE[coin50][coin100] = None


sys.setrecursionlimit(10*MAX_N)
while (s := sys.stdin.readline().strip()):
    clear(s)
    sys.stdout.write(f'{solve()}\n')
