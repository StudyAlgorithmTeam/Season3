from collections import deque, defaultdict
import sys

# V = N = 1,000
# E = M = 500,000
N, M = map(int, sys.stdin.readline().split())

E = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    E[A].append(B)


# O(V+E) Find sources via BFS (source: 선행 과목이 없는 과목)
is_source = [True] * (N+1)
visited = defaultdict(bool)
queue = deque(range(1, N+1))
while queue:
    u = queue.popleft()
    for v in E[u]:
        if not visited[v]:
            queue.append(v)
            visited[v] = True
            is_source[v] = False

# O(V^2) Find longest distances from sources via Djijkstra-like
dist = [1] * (N+1)
for i in range(1, N+1):
    if is_source[i]:
        queue.append(i)
while queue:
    u = queue.popleft()
    for v in E[u]:
        if dist[v] < dist[u] + 1:
            queue.append(v)
            dist[v] = dist[u] + 1

print(*dist[1:])
