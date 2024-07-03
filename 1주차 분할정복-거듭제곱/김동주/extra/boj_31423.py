# 신촌 통폐합 계획

import sys

IDX_STRING = 0
IDX_NEXT = 1
IDX_TAIL = 2
IDX_EMPTY = 3

N = int(sys.stdin.readline())

# s, next, tail, empty
S = [None] + [[sys.stdin.readline().strip(), None, i, False] for i in range(1, N+1)]

for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    S[S[i][IDX_TAIL]][IDX_NEXT] = j
    S[i][IDX_TAIL] = S[j][IDX_TAIL]
    S[j][IDX_EMPTY] = True

# i문자열을 출력
while i is not None:
    sys.stdout.write(S[i][IDX_STRING])
    i = S[i][IDX_NEXT]
sys.stdout.write('\n')
