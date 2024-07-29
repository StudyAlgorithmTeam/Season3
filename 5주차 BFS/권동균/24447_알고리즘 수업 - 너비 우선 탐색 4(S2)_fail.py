from collections import deque, defaultdict
import sys
input=sys.stdin.readline

N,M,R=map(int, input().split())

t=[]

E = defaultdict(list)
q = deque()
visited = [-1] * (N)

for i in range(M):
    u,v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

visited[R] = 1
q.append(R)
depth = 0

while q:
    width = len(q)
    for _ in range(width):
        u = q.popleft()
        if visited[u]!=-1:
            t.append(u*depth)
        else:
            depth=-1
            t.append(u*depth)
        for v in E[u]:
            if visited[v]==-1:
                visited[v] = 1
                q.append(v)
    depth += 1

print(sum(t))
