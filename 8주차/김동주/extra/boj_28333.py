# 화이트 칼라

from collections import deque
import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    R = 1
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        E = [[] for u in range(N+1)]
        E_R = [[] for u in range(N+1)]  # Reverse edge
        for i in range(M):
            u, v = map(int, sys.stdin.readline().split())
            E[u].append(v)
            E_R[v].append(u)

        # Dijkstra
        queue = deque()
        dist = [sys.maxsize] * (N+1)
        dist[R] = 0
        queue.append(R)
        while queue:
            u = queue.popleft()
            if u == N:
                break
            for v in E[u]:
                if dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        # BFS in Reverse order (dist를 통해 최단 경로(들)로만 이동)
        queue.clear()
        visited = [False] * (N+1)
        visited[N] = True
        queue.append(N)
        while queue:
            u = queue.popleft()
            for v in E_R[u]:
                if not visited[v] and dist[v] == dist[u]-1:
                    visited[v] = True
                    queue.append(v)
        # Print visited verticies
        sys.stdout.write(' '.join(str(i) for i in range(1, N+1) if visited[i])+'\n')
