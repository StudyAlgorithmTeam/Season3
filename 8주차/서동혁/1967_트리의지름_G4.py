import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # n < 10,000

edges = [[] for _ in range(n+1)]

visited = [-1] * (n+1)
visited[1] = 0

for i in range(n-1): # O(N*N) ??
    parent, child, cost = map(int,input().split()) # split 함수의 시간 복잡도 -> O(N)
    edges[parent].append([child,cost])
    edges[child].append([parent,cost])

def dfs(root, dist):
    for i, w in edges[root]:
        if visited[i] == -1:
            visited[i] = dist + w
            dfs(i, dist + w)

dfs(1,0) # O(V + E) -> O(N + N-1) -> O(N)

m = max(visited)
m_node = visited.index(m)

visited = [-1] * (n+1)
visited[m_node] = 0

dfs(m_node,0) # O(V + E) -> O(N + N-1) -> O(N)

print(max(visited))