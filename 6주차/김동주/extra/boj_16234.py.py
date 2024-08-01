# 인구 이동

# O(2000*(4V+E)), 이 때 V = O(N^2), E = O(4N^2) 이다.
# 따라서 최종 시간 복잡도는 O(N^2)이다.
# 얼마 안되는 것 같지만, 계수를 포함해보면 상당히 타이트 한 시간이다.
# O(16000 * N^2), N <= 50 => T(40,000,000)

from collections import deque
import sys


# O(V)
N, L, R = map(int, sys.stdin.readline().split())
A = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
B = [[0]*N for _ in range(N)]


# O(2000*(V+E)) 최대 2000번까지만 이동하는 경우만 주어짐.
moves = 0
stack = []
queue = deque([])
visited = [[False]*N for _ in range(N)]
while True:
    # O(V) initialize for each iteration
    for r in range(N):
        for c in range(N):
            visited[r][c] = False
    is_moved = False

    # O(V+E)
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            # O(V+E) BFS
            queue.append((r, c))
            stack.append((r, c))
            visited[r][c] = True
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    nr, nc = r+dr, c+dc
                    if bool(
                        0 <= nr < N and
                        0 <= nc < N and
                        not visited[nr][nc] and
                        L <= abs(A[r][c] - A[nr][nc]) <= R
                    ):
                        queue.append((nr, nc))
                        stack.append((nr, nc))
                        visited[nr][nc] = True

            if len(stack) > 1:
                is_moved = True

            # O(V) 새로운 인구수 계산 : (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
            a = sum(A[r][c] for r, c in stack) // len(stack)

            # O(V) 인구 이동
            while stack:
                r, c = stack.pop()
                B[r][c] = a

    if not is_moved:
        break

    A, B = B, A
    moves += 1

print(moves)
