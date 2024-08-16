# 전깃줄

from functools import cache
import sys


A = 0
B = 1

N = int(sys.stdin.readline())
A_to_B = []

for u in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A_to_B.append((a, b))

A_to_B.sort()


@cache
def lis(i: int, start: int) -> int:
    # longest increasing subsequence
    # i = O(N)
    # start = O(500)
    if i == N:
        return 0
    max_len = lis(i+1, start)
    if A_to_B[i][B] >= start:
        max_len = max(max_len, lis(i+1, A_to_B[i][B])+1)
    return max_len


print(N - lis(0, 0))
