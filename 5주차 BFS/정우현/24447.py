from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
N, M, V = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]

# 간선 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = G[b][a] = 1

# 깊이와 방문 순서를 저장할 배열 초기화
depth = [-1] * (N + 1)  # 깊이 배열
visited = [0] * (N + 1)  # 방문 순서 배열

# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    depth[start] = 0  # 시작 정점의 깊이는 0
    visited[start] = 1  # 시작 정점의 방문 순서는 1
    order = 2  # 방문 순서의 초기값
    
    while queue:
        node = queue.popleft()
        for i in range(1, N + 1):
            if G[node][i] == 1 and depth[i] == -1:  # 인접 정점이며 방문하지 않은 경우
                depth[i] = depth[node] + 1  # 깊이 설정
                visited[i] = order  # 방문 순서 설정
                order += 1
                queue.append(i)

# BFS 실행
bfs(V)

# d_i * t_i의 합 계산
result = 0
for i in range(1, N + 1):
    if depth[i] != -1:  # 방문한 정점만 계산
        result += depth[i] * visited[i]

# 결과 출력
print(result)
