import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

#입력이 괄호와 쉼표가 포함됨....

# T = 100
# P = 100,000
# N = 100,000

# 1,000,000
#   100,000

# O(T PN -> T(P+N))
for i in range(t):
    p = input()
    n = int(input())
    myArr = input().strip()

    if myArr == '[]': #빈 배열 처리
        arr = deque()
    else:
        # O(N)
        arr = deque(map(int, myArr[1:-1].split(',')))
    #arr = deque(map(int,input().strip()[1:-1].split(','))) <- 이렇게 하면 빈 배열은 처리하지 못함.
#replace('[', '').replace(']', '').replace(',','') fail 파싱 찾아봄

    # O(P*N) -> O(P)
    for j in p:
        if j == 'R':
            # O(1) 으로 할 수 있는 방법을 찾아야...
            arr.reverse() # O(N/2)
        elif j == 'D':
            if len(arr) == 0:
                break
            else:
                arr.popleft() # O(1)
    if len(arr) == 0:
        print('error')
    else:
        # O(N)
        print(arr)
