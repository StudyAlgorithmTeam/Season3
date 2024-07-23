N, M = map(int,input().split())
table = []

for _ in range(N):
    table.append(list(input()))

count = 0

def check(i,j):
    if i > N - 1 or j > M - 1:
        return 0
    
    if table[i][j] == '*':
        table[i][j] = '.'
        check(i,j+1)
        check(i+1,j)
        check(i+1,j+1)
    
for i in range(N):
    for j in range(M):
        if table[i][j] == '*':
            count += 1
            check(i,j)

print(count)    