# 절망적인 줄

import sys


MOD = 1000000
MAX_N = 1000


def solve(s: str):
    n = len(s)
    # 각 배열의 i번째 원소는 100원짜리 동전이 i개일 때의 경우의 수임.
    dp_next = [0] * (n//2+2)
    dp_prev = [0] * (n//2+2)

    dp_prev[0] = 1
    for i in range(n):
        max_coin100 = (i+1)//2 # 100원짜리 최대 개수 (50원 개수 이하여야만 함.)
        if s[i] == '(':
            for coin100 in range(max_coin100+1):
                dp_next[coin100] = dp_prev[coin100]
        elif s[i] == ')':
            for coin100 in range(max_coin100+1):
                dp_next[coin100] = dp_prev[coin100-1]
        else:
            for coin100 in range(max_coin100+1):
                dp_next[coin100] = (dp_prev[coin100-1] + dp_prev[coin100]) % MOD
        dp_next, dp_prev = dp_prev, dp_next
    return dp_prev[n//2]


while (s := sys.stdin.readline().strip()):
    sys.stdout.write(f'{solve(s)}\n')
