# 루나의 게임 세팅

import sys
import math


MAX_N = 2000
MOD = int(1e9+7)


def solve(N: int, K: int) -> int:
    """브루즈칼리파처럼
     |
    ||
    |||
    ㄴ 이런 식으로 지으라는 것으로 이해함.

    >>> solve(5, 3)
    40
    """
    # 가장 큰 것을 중심으로, 가장 큰 것을 제외한 나머지 K-1개를
    # 앞서 완성한 타워의 어디(앞/뒤)에 붙일지에 대한 경우의 수
    return (math.comb(N, K) % MOD) * pow(2, K-1, MOD) % MOD


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    # A = [*map(int, sys.stdin.readline().split())]
    print(solve(N, K))
