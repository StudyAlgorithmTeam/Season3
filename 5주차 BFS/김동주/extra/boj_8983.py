# 사냥꾼
# O(N log NM)

import bisect
import sys


M, N, L = map(int, sys.stdin.readline().split())
X = [*map(int, sys.stdin.readline().split())]

# O(N log N)
X.sort()

count = 0
# O(N log M)
for j in range(N):
    a, b = map(int, sys.stdin.readline().split())
    # O(log M)
    # 이진 탐색으로 사대의 위치 x_i와 가장 가까운 a_j 값을 찾아 거리를 계산한다.
    i = bisect.bisect(X, a)  # X[:i] <= a
    dist = min([abs(X[i+di]-a)+b for di in (-1, 0, 1) if 0 <= i+di < M])
    if L >= dist:
        count += 1

print(count)
