# 죽음의 게임

# O(V+E) where V=O(N) E=O(N)

from collections import deque
import sys


N, K = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)] # O(V)


# O(V+E) - Breadth First Search.
queue = deque([])
dist = [sys.maxsize]*N

queue.append(0)
dist[0] = 0
while queue:
    u = queue.popleft()
    v = A[u]
    if dist[v] == sys.maxsize:
        dist[v] = dist[u] + 1
        queue.append(v)

if dist[K] == sys.maxsize:
    print(-1)
else:
    print(dist[K])
