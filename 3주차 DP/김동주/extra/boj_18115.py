# 카드 놓기

from collections import deque


N = int(input())
A = input().split()

# double-ended queue
# 0번 인덱스가 위이다.
dq = deque()

for i in range(1, N+1):
    match A.pop():
        # 제일 위의 카드 1장을 바닥에 내려놓는다.
        case "1":
            dq.appendleft(i)

        # 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
        case "2":
            dq.insert(1, i)

        # 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
        case "3":
            dq.append(i)

print(*dq)
