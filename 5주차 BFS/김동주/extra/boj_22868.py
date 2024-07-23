# 산책 (small)

from collections import deque
from typing import List
import sys


def solve(N: int, M: int, A: List[int], B: List[int], S: int, E: int) -> int:
    """
    >>> solve(4,5,[1,1,2,2,3],[2,3,3,4,4,4],1,4)
    4

    아래의 그래프는 Dijkstra 만으로는 풀기 어렵다.
    :    S       :    S       :
    :  +-1---+   :  +-1---+   :
    :  | |   |   :  | |   |   :
    :  2 5-+ 9   :  | 5-+ |   :
    :  | | | |   :  | | | |   :
    :  3-4 6 10  :  +-4 | |   :
    :    | | |   :    | | |   :
    :    8-7 11  :    +-8-+   :
    :    |   |   :      E     :
    :    |   12  :            :
    :    |   |   :            :
    :    +---13  :            :
    :      E     :            :
    answer: 8
    1 -> 2 -> 3 -> 4 -> 8 -> 7 -> 6 -> 5 -> 1

    >>> solve(13,15,[1,1,1,2,3,4,4,5,6,7,8,9,10,11,12],[2,5,9,3,4,5,8,6,7,8,13,10,11,12,13],1,8)
    8

    """
    edges = [[] for i in range(N+1)]
    for i in range(M):
        edges[A[i]].append(B[i])
        edges[B[i]].append(A[i])
    for i in range(1, N+1):
        edges[i].sort()

    visited = [False]*(N+1)
    parent = [None]*(N+1)

    dist_s2e = bfs(E=edges, s=S, t=E, visited=visited, parent=parent)

    visited = [False]*(N+1)
    p = E
    while p != S:
        visited[p] = True
        p = parent[p]

    dist_e2s = bfs(E=edges, s=E, t=S, visited=visited, parent=parent)

    return dist_s2e + dist_e2s


def bfs(E: List[List[int]], s: int, t: int, visited: List[bool], parent: List[int | None]) -> int:
    # s: source, t: sink
    queue = deque()
    # Starting vertex
    visited[s] = True
    queue.append(s)
    dist = 0
    while queue:
        for _ in range(len(queue)):
            u = queue.popleft()
            if u == t:
                return dist
            for v in E[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    # Update paths
                    parent[v] = u
        dist += 1
    raise ValueError("no path found.")


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    A, B = [0]*M, [0]*M
    for i in range(M):
        A[i], B[i] = map(int, sys.stdin.readline().split())
    S, E = map(int, sys.stdin.readline().split())
    print(solve(N, M, A, B, S, E))
