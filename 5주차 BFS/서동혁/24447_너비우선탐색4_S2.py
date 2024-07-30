from collections import defaultdict, deque

N, M, R = map(int,input().split())

visited = [-1] * (N+1)
edges = defaultdict(list)
result = []
depth = 0
count = 1

for _ in range(M):
    u, v = map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N+1):
    edges[i].sort()

q = deque([[R,1,0]])

while q:
    temp = q.popleft()
    n = temp[0]
    count = temp[1]
    dep = temp[2]
    depth += 1
    
    if not visited[n] or visited[n] == -1:
        visited[n] = 1
        result.append([count,dep])

        for i in edges[n]:
            if visited[i] == -1:
                visited[i] = 0
                count += 1
                q.append([i,count,depth])

print(result)