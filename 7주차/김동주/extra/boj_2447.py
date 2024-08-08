# 별 찍기 - 10

import sys


def is_filled(x: int, y: int, N: int) -> bool:
    if N == 1:
        return True
    n = N // 3
    if n <= x < 2*n and n <= y < 2*n:
        return False
    return is_filled(x % n, y % n, n)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for y in range(N):
        for x in range(N):
            sys.stdout.write('*' if is_filled(x, y, N) else ' ')
        sys.stdout.write('\n')
