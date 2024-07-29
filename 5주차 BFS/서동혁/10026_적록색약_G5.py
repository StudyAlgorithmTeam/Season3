from collections import deque

N = int(input())
q = deque()

visit = [[0]*N for _ in range(N)]

color_table = []

for i in range(N):
    color_table.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q.append((x,y))
    visit[x][y] = 1

    while q:
        x, y = q.popleft()
        for index in range(4):
            new_x = x + dx[index]
            new_y = y + dy[index]

            if 0 <= new_x < N and 0 <= new_y < N and not visit[new_x][new_y] and color_table[x][y] == color_table[new_x][new_y]:
                q.append((new_x, new_y))
                visit[new_x][new_y] = 1

count = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i,j)
            count += 1

for i in range(N):
    for j in range(N):
        if color_table[i][j] == 'G':
            color_table[i][j] = 'R'

visit = [[0]*N for _ in range(N)]


blindness_count = 0

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i,j)
            blindness_count += 1

print(count, blindness_count)