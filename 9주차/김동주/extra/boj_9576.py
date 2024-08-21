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
        timelines.append((start, end))
    timelines.sort()
    now = 0
    count = 0
    for start, end in timelines:
        if now < start:
            now = start
            count += 1
        elif start <= now < end:
            now = now + 1
            count += 1
    sys.stdout.write(f'{count}\n')
