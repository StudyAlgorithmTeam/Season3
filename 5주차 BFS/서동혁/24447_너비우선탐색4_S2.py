from collections import defaultdict, deque

N, M, R = map(int, input().split())

visited = [-1] * (N+1)
edges = defaultdict(list)
result = 0
depth = 0
t_i = 1

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N+1):
    edges[i].sort()

q = deque([[R, 1, 0]])

while q:
    u, t_i, d_i = q.popleft()

    if not visited[u] or visited[u] == -1:
        visited[u] = 1
        result += t_i * d_i

        for i in edges[u]:
            if visited[i] == -1:
                visited[i] = 0
                t_i += 1
                q.append([i, t_i, d_i+1])

print(result)
