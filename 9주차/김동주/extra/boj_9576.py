# 책 나눠주기

import sys


T = int(sys.stdin.readline())
for _ in range(T):
    # 회의실 배정 문제로 치환하여 풀이.
    # 최대 몇 개의 회의를 진행할 수 있을까!
    N, M = map(int, sys.stdin.readline().split())

    timelines = []
    for i in range(M):
        start, end = map(int, sys.stdin.readline().split())
        timelines.append([start, end])
    timelines.sort(key=lambda x: (x[1], x[0]))

    selected = [False] * (N+1)
    for start, end in timelines:
        for n in range(start, end+1):
            if not selected[n]:
                selected[n] = True
                break

    count = 0
    for n in range(1, N+1):
        if selected[n]:
            count += 1

    sys.stdout.write(f'{count}\n')
