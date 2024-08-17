# 역사

from functools import cache
import sys

# 사건들의 전후관계간 방향그래프를 만든다.

N, K = map(int, sys.stdin.readline().split())
E = [[] for _ in range(N+1)]
for _ in range(K):
    u, v = map(int, sys.stdin.readline().split())
    E[u].append(v)

# 물음에 답하기 위해 그래프 순회를 실시한다. (백트래킹)

visited = [False] * (N+1)

@cache
def happens_before(snode: int, enode: int) -> bool:
    # 향후 간선이 갱신 될 일은 없으므로 캐시해서 사용.
    if snode == enode:
        return True
    for child in E[snode]:
        if not visited[child]:
            if happens_before(child, enode):
                return True
    return False

S = int(sys.stdin.readline())
for _ in range(S):
    s, t = map(int, sys.stdin.readline().split())
    if happens_before(s, t):
        sys.stdout.write("-1\n")
    elif happens_before(t, s):
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
