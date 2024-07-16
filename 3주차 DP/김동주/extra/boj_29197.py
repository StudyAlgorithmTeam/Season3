# 아침 태권도

import sys
import math


def solve(N: int, X: int, Y: int) -> int:
    """사범이 볼 수 있는 학생 수를 반환한다.

    >>> solve(7, [1,2,-2,-4,-1,-3,2], [2,4,2,4,0,0,-1])
    4
    >>> solve(5, [1,2,1,3,2], [2,4,1,2,2])
    3
    """
    rads = set()
    for i in range(N):
        rad = math.atan2(Y[i], X[i])
        rads.add(rad)
    return len(rads)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, sys.stdin.readline().split())
    print(solve(N, X, Y))
