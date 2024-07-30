from collections import deque
from typing import List
import sys


def bfs(N: int, E: List[List[int]], R: int) -> int:
    # O(N+M) : 이 함수의 전체 시간복잡도

    # O(N)
    d = [0] * (N+1)  # d[i]: i번 노드의 깊이
    t = [0] * (N+1)  # 방문 순서

    Q = deque()
    n_visited = 0

    # 한 노드 방문
    Q.append(R)
    d[R] = 0  # 시작 정점의 깊이는 0
    t[R] = 1  # 시작 정점의 방문 순서는 1
    n_visited += 1 # 방문한 노드의 개수

    # O(V+E) = O(N+M) 모든 간선, 모든 정점에 대하여 한 번씩만 방문
    while Q:
        u = Q.popleft() # O(N * O(1)) = O(N)
        for v in E[u]:
            pass # O(M)
            if t[v] == 0:
                # 한 노드 방문
                Q.append(v)
                d[v] = d[u] + 1
                t[v] = n_visited + 1
                n_visited += 1

    # O(N)
    return sum(d[i]*t[i] for i in range(1, N+1))


# O(N+M log M) : 풀이 전체의 시간복잡도
if __name__ == "__main__":
    N, M, R = map(int, sys.stdin.readline().split())
    E = [[] for _ in range(N+1)]  # O(N)
    # O(M)
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        # Undirected Graph이므로 양방향 모두 추가
        E[u].append(v)
        E[v].append(u)
    # O(N + M log M)
    for i in range(1, N+1):
        # 정점은 오름차순으로 방문한다고 했으므로
        E[i].sort() # O(M log M)
    # O(N+M)
    print(bfs(N, E, R))
