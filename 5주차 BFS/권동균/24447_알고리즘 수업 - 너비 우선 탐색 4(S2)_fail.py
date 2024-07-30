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
q.append((R,1 )) # 큐 안에는 노드(정점 번호)가 들어있음
depth = 0

# BFS
while q:
    width = len(q)
    for _ in range(width):
        u, t_i = q.popleft() # node (방문 순서대로 큐에 꺼내오고... -> 이게 방문 순서라고 생각)
        if visited[u]!=-1:
            t.append(u*depth) #
        else:
            depth=-1
            t.append(u*depth)
        for v in E[u]:
            if visited[v]==-1:
                visited[v] = 1
                q.append((v, t_i+1))
    depth += 1

print(sum(t))
