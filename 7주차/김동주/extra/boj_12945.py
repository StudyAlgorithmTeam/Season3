# 재미있는 박스 정리

import sys
import math


N, *V = map(int, sys.stdin.read().split())
V.sort()

l = 0
for r in range(math.ceil(N/2), N):
    if V[r] >= 2*V[l]:
        l += 1

print(N-l)
