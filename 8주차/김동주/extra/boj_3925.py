# 암호화의 취약점 찾기

import sys
from typing import List


def find_key(M: List[int]) -> int:
    K = 0
    for j in range(32):
        K |= (sum(M[i] ^ K for i in range(8)) ^ M[8]) & (1 << j)
    return K


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    numbers = [*map(lambda x: int(x, base=16), sys.stdin.read().split())]
    for t in range(T):
        M = numbers[9*t:9*(t+1)]
        K = find_key(M)
        sys.stdout.write(f'{K:x}\n')
