# RGB거리

import sys


N = int(sys.stdin.readline())

fr, fg, fb = 0, 0, 0
for i in range(N):
    cr, cg, cb = map(int, sys.stdin.readline().split())
    fr, fg, fb = cr+min(fg, fb), cg+min(fr, fb), cb+min(fr, fg)

print(min(fr, fg, fb))
