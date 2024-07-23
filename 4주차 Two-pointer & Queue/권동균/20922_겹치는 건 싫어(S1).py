from collections import deque

N, K = map(int, input().split())
l = list(map(int, input().split()))

r = deque()
idx = [0] * 100001
M = 0

for i in l:
    while idx[i] == K:
        idx[r.popleft()] -= 1
    idx[i] += 1
    r.append(i)
    M = max(M, len(r))

print(r)
