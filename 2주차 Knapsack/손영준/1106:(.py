import math
INF = float('inf')
dp = [[INF for _ in range(c+1)]for _ in range(n+1)]
#원하는 인원수를 최소 비용으로 구하는 방법

c,n = map(int, input().split())
hotel = [] #cost, benefit

for i in range(n):
    cost, people = map(int, input().split())
    hotel.append(cost,people)
