import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0]*n for _ in range(n)]

#모든 경로를 만들어 준다.
#시간 복잡도 : m만큼 반복 O(m)
for _ in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1
    
#i,k 와 k,j가 있다고 했을 때 i,j도 경로로 설정해 준다.
#시간 복잡도 : 3중 for문으로 O(n^3)이 걸린다. 
#n의 최대가 400이여서 가능한 문제이다.
#플로이드 워셜 알고리즘을 활용하였다.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] and a[k][j]:
                a[i][j] = 1
                
#경로가 있는지 확인하는 배열
#시간 복잡도 : s만큼 반복 O(s)
s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if a[x-1][y-1] == 1:
        print(-1)
    elif a[y-1][x-1] == 1:
        print(1)
    elif a[x-1][y-1] == 0:
        print(0)