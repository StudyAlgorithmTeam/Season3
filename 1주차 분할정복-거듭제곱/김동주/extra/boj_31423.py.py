# 신촌 통폐합 계획

import sys

IDX_STRING = 0
IDX_NEXT = 1
IDX_TAIL = 2
IDX_EMPTY = 3

N = int(sys.stdin.readline())

# s, next, tail, empty
S = [[sys.stdin.readline(), None, i, False] for i in range(N)]

for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    i = i-1
    j = j-1
    S[S[i][IDX_TAIL]][IDX_NEXT] = j
    S[i][IDX_TAIL] = S[j][IDX_TAIL]
    S[j][IDX_EMPTY] = True

# i문자열을 출력
while i is not None:
    sys.stdout.write(S[i][IDX_STRING].strip())
    i = S[i][IDX_NEXT]
sys.stdout.write('\n')
