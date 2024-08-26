# 수상 택시

import sys

S, E = 0, 1
N, M = map(int, sys.stdin.readline().split())

# 1. 모든 숫자는 0..M 이므로, 전진하는 경우는 0에서 M까지 이동 중에 자연스레 처리된다.
# 2. 역방향으로 거슬러가서 내려야 하는 사람들의 경우를 최소 거리로 처리하여야 한다.

# 2-1. 역방향으로 승하차 하는 승객을 구분한다.
backward = []

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    if s > e:
        backward.append((s, e))

# 2-2. 구간이 겹치는 승객들은 최대한 한 번에 태울 수 있도록 구간을 합친다.
backward_compressed = []
for s, e in sorted(backward, key=lambda x: -x[S]):
    if backward_compressed and backward_compressed[-1][E] <= s:
        s = backward_compressed[-1][S]
        e = min(e, backward_compressed[-1][E])
        backward_compressed.pop()
    backward_compressed.append((s, e))

# 2-3. 역방향 구간들을 왕복한다.
dist = M  # 전진하는 경우 이동해야하는 길이
for s, e in backward_compressed:
    dist += 2 * (s-e)

print(dist)
