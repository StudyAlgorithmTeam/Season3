from collections import defaultdict, deque
import sys
import heapq


def bfs(V, E, R):
    d = defaultdict(lambda: 0)
    t = defaultdict(lambda: -1)

    Q = deque([R])
    t[R] = 1

    depth = 0
    last_visited = R
    while Q:
        for _ in range(len(Q)):
            u = Q.popleft()
            while E[u]:
                v = heapq.heappop(E[u])
                if t[v] == -1:
                    d[v] = depth+1
                    t[v] = t[last_visited] + 1
                    last_visited = v
                    Q.append(v)
        depth += 1

    return sum(d[i]*t[i] for i in V)


if __name__ == "__main__":
    N, M, R = map(int, sys.stdin.readline().split())
    V = set(range(1, N+1))
    E = defaultdict(list)
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        heapq.heappush(E[u], v)
        heapq.heappush(E[v], u)
    print(bfs(V, E, R))
