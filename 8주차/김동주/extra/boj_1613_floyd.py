# 역사

import sys

# 사건들의 전후관계간 방향그래프를 만든다 (인접행렬).

N, K = map(int, sys.stdin.readline().split())

adjmat = [[False] * (N+1) for _ in range(N+1)]

for _ in range(K):
    u, v = map(int, sys.stdin.readline().split())
    adjmat[u][v] = True

# 플로이드 워셜 알고리즘으로 미리 모든 정점간 연결관계를 파악한다.

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not adjmat[i][j] and adjmat[i][k] and adjmat[k][j]:
                adjmat[i][j] = True

# 물음에 답하기 위해 두 정점의 연결 관계를 조회한다.

S = int(sys.stdin.readline())
for _ in range(S):
    s, t = map(int, sys.stdin.readline().split())
    if adjmat[s][t]:
        sys.stdout.write("-1\n")
    elif adjmat[t][s]:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
