import sys
input = sys.stdin.readline

N = int(input())

color = []

for _ in range(N):
    color.append(list(map(int,input().split())))

DP = [[0]*N for i in range(3)]

DP[0][0] = color[0][0]
DP[1][0] = color[0][1]
DP[2][0] = color[0][2]

for i in range(1,N):
    DP[0][i] = min(DP[1][i-1]+color[i][0], DP[2][i-1]+color[i][0])
    DP[1][i] = min(DP[0][i-1]+color[i][1], DP[2][i-1]+color[i][1])
    DP[2][i] = min(DP[0][i-1]+color[i][2], DP[1][i-1]+color[i][2])

print(min(DP[0][N-1], DP[1][N-1], DP[2][N-1]))