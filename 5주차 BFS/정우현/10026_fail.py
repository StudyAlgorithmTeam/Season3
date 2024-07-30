N = int(input())
m_arr = []

for i in range(N):
    w = list(input())
    m_arr.append(w)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]


v = [[0]*N for _ in range(N)]
def bfs(x,y):
    q = []
    q.append((x,y))
    v[x][y] = 1


    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and m_arr[nx][ny] == m_arr[x][y] and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1
       
v2 = [[0]*N for _ in range(N)]                
def bfs_2(x,y):
    q = []
    q.append((x,y))
    v2[x][y] = 1


    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and v2[nx][ny] == 0:
                if m_arr[nx][ny] != 'B' or m_arr[nx][ny] == m_arr[x][y]:
                    q.append((nx,ny))
                    v2[nx][ny] = 1

result = []
count = 0
for i in range(N):
    for j in range(N):
        if v[i][j] ==0:
            bfs(i,j)
            count += 1
    
result.append(count)

count = 0
for i in range(N):
    for j in range(N):
        if v[i][j] ==0:
            bfs_2(i,j)
            count += 1
            
result.append(count)
print(result)