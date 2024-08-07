# 전역 역전

import sys
from datetime import date
from functools import cache


sys.setrecursionlimit(int(1e6))

종현 = date(*map(int, sys.stdin.readline().split())).toordinal()
영도 = date(*map(int, sys.stdin.readline().split())).toordinal()
T, N = map(int, sys.stdin.readline().split())
ops = [[*map(int, sys.stdin.readline().split())] for i in range(N)]


@cache
def knapsack(i: int, T: int) -> int:
    """영도가 얼마나 더 빨리 전역하는가 ...의 최댓값.

    = max((종현의 전역일) - (영도의 전역일))
    """
    if T < 0:
        return -sys.maxsize
    if i == N:
        return 종현-영도
    # i번째 행동을 한다.
    match ops[i][0]:
        case 1:
            do_something = knapsack(i+1, T-ops[i][1]) + ops[i][2]
        case 2:
            do_something = knapsack(i+1, T-ops[i][1]) + ops[i][2]
        case 3:
            do_something = knapsack(i+1, T-ops[i][1]) + 30*ops[i][2]
    # i번째 행동을 하지 않는다.
    do_nothing = knapsack(i+1, T)
    return max(do_nothing, do_something)


if __name__ == "__main__":
    diff = knapsack(0, T)
    # 영도가 종현보다 앞서 전역할 수 있다면
    if diff > 0:
        print(diff)
    # 영도가 종현보다 앞서 전역할 수 없다면
    else:
        print(-diff)
