n = int(input())
color = []
#using DP!
for _ in range(n):
    color.append(list(map(int,input().split())))
    
for i in range(1,n):
    color[i][0] = min(color[i-1][1],color[i-1][2])+color[i][0] #RED=0
    color[i][1] = min(color[i-1][0],color[i-1][2])+color[i][1] #GREEN=1
    color[i][2] = min(color[i-1][0],color[i-1][1])+color[i][2] #BLUE=2
    
print(min(color[n-1])) #마지막 집 칠하는 경우 中 최소
