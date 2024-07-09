# 카드 정렬하기

import sys
from heapq import heappop, heappush, heapify


N, *heap = map(int, sys.stdin.read().split())

heapify(heap)
n_total_compares = 0

while len(heap) > 1:
    n_compares = heappop(heap) + heappop(heap)
    heappush(heap, n_compares)
    n_total_compares += n_compares

print(n_total_compares)
