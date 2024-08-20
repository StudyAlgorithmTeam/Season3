# 부분합

import sys
from collections import deque


N, S, *A = map(int, sys.stdin.read().split())

queue = deque()
queue_sum = 0
queue_min_len = sys.maxsize

for i in range(N):
    queue.append(A[i])
    queue_sum += A[i]
    while len(queue) > 0 and queue_sum >= S:
        if queue_min_len > len(queue):
            queue_min_len = len(queue)
        queue_sum -= queue.popleft()

if queue_min_len == sys.maxsize:
    print(0)
else:
    print(queue_min_len)
