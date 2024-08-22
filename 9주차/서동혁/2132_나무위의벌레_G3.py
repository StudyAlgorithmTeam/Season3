import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

n = int(input())
# n < 10,000

fruits = [0] + list(map(int,input().split())) # O(N)
edges = [[] for _ in range(n+1)] # O(N)

for i in range(n-1): # O(N)
    s,e = map(int,input().split())
    edges[s].append(e)
    edges[e].append(s)

visited = [-1] * (n+1)

def dfs(root,count): # O(V + E) -> O(N + N-1) -> O(N)
    if visited[root] == -1:
        visited[root] = count + fruits[root]
        for i in edges[root]:
            dfs(i, count + fruits[root])

dfs(1,0)

MAX_INDEX1 = visited.index(max(visited))

visited = [-1] * (n+1)

dfs(MAX_INDEX1, 0)

MAX_INDEX2 = visited.index(max(visited))

print(max(visited), min(MAX_INDEX1, MAX_INDEX2))