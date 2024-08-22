# 짝수 팰린드롬

import collections


N = int(input())
A = [*map(int, input().split())]

deque = collections.deque()
count = 0

try:
    assert N % 2 == 0
    for i in range(0, N, 2):
        deque.append(A[i])
        deque.append(A[i+1])
        if deque[0] != deque[-1]:
            continue
        stack = []
        while deque and deque[0] == deque[-1]:
            stack.append(deque[0])
            deque.popleft()
            deque.pop()
        if not deque:
            count += 1
            continue
        while stack:
            x = stack.pop()
            deque.append(x)
            deque.appendleft(x)
    assert not deque
except AssertionError:
    print(-1)
else:
    print(count)
