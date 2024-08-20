# 크리스마스 선물

import sys
import heapq

heap = []

N = int(sys.stdin.readline())
for i in range(N):
    a, *A = map(int, sys.stdin.readline().split())
    if a == 0:
        if len(heap) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(f'{-heapq.heappop(heap)}\n')
    else:
        for i in range(a):
            heapq.heappush(heap, -A[i])
