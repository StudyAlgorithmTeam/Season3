# 무한부스터

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
a = [[None] * M for _ in range(N)]
for i in range(N):
    for j, a_ij in enumerate(map(int, sys.stdin.readline().split())):
        a[i][j] = a_ij

# dijkstra O(V^2)
dist = [[sys.maxsize] * M for _ in range(N)]
dist[0][0] = 0
queue = deque([(0, 0)])
while queue:
    for _ in range(len(queue)):
        i, j = queue.popleft()
        if i == N-1 and j == M-1:
            break
        for x in range(1, a[i][j]+1):
            # 오른쪽으로 x칸 이동
            if j+x < M and dist[i][j+x] > dist[i][j]+1:
                dist[i][j+x] = dist[i][j]+1
                queue.append((i, j+x))
            # 아래쪽으로 x칸 이동
            if i+x < N and dist[i+x][j] > dist[i][j]+1:
                dist[i+x][j] = dist[i][j]+1
                queue.append((i+x, j))

print(dist[N-1][M-1])
