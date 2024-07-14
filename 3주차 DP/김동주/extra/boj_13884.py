# 삭삽 정렬

import collections
import sys


def solve(A: list):
    N = len(A)
    indicies = collections.defaultdict(list)
    for idx, num in enumerate(A):
        # 인덱스 순으로 접근하므로, 자연스럽게 정렬되어있다.
        indicies[num].append(idx)
    ops = 0 # 삭삽이 필요한 원소의 개수 (우웁스 아님.)
    noops = 0 # 삭삽이 필요없는 원소의 개수
    last_idx = -1
    for num in sorted(indicies):
        for idx in indicies[num]:
            if idx > last_idx:
                noops += 1
                last_idx = idx
            else:
                ops += 1
        if ops > 0:
            ops = N-noops
            break
    return ops


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        K, N = map(int, sys.stdin.readline().split())
        A = []
        for i in range(((N-1)//10)+1):
            A.extend(map(int, sys.stdin.readline().split()))
        sys.stdout.write(f'{K} {solve(A)}\n')
