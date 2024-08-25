# 파일 합치기

import heapq
import sys
import typing


def solve(K: int, FILE_SIZES: typing.List[int]) -> int:
    cost = 0
    heap = [*FILE_SIZES]
    heapq.heapify(heap)
    while len(heap) > 1:
        x1 = heapq.heappop(heap)
        x2 = heapq.heappop(heap)
        y = x1 + x2
        cost += y
        heapq.heappush(heap, y)
    return cost


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        FILE_SIZES = [*map(int, sys.stdin.readline().split())]
        print(solve(K, FILE_SIZES))
