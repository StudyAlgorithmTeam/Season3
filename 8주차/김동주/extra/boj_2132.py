# 나무 위의 벌레

import sys


MAX_N = 10000

N = int(sys.stdin.readline())
V = [None, *map(int, sys.stdin.readline().split())] # value of a node
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    E[A].append(B)
    E[B].append(A)

# 트리라고 하였으니, 사이클이 없는 무방향 연결 그래프인 것을 가정한다.
# 모든 노드는 연결되어있으므로, 다음의 방법으로 문제의 답을 구한다.
# 1. 임의의 점에서 DFS로 가장 많은 열매를 먹을 수 있는 경로를 찾는다.
# 2. 해당 경로의 끝에서 다시 가장 많은 열매를 먹을 수 있는 경로를 찾는다.

sys.setrecursionlimit(4*MAX_N)


def dfs(u: int):
    best_eats = V[u]
    best_node = u
    for v in E[u]:
        if visited[v]:
            continue
        visited[v] = True
        eats, node = dfs(v)
        if (best_eats < V[u]+eats) or (best_eats == V[u]+eats and best_node > node):
            best_eats = V[u]+eats
            best_node = node
    return best_eats, best_node

visited = [False] * (N+1)
visited[1] = True
_, u = dfs(1)

visited = [False] * (N+1)
visited[u] = True
eats, v = dfs(u)

print(eats, min(u, v))
