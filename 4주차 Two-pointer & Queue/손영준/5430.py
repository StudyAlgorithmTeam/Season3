import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

#입력이 괄호와 쉼표가 포함됨....
for i in range(t):
    p = input()
    n = int(input())
    myArr = input().strip()
    
    if myArr == '[]': #빈 배열 처리
        arr = deque()
    else:
        arr = deque(map(int, myArr[1:-1].split(',')))
    #arr = deque(map(int,input().strip()[1:-1].split(','))) <- 이렇게 하면 빈 배열은 처리하지 못함.
#replace('[', '').replace(']', '').replace(',','') fail 파싱 찾아봄
    for j in p:
        if j == 'R':
            arr.reverse()
        elif j == 'D':
            if len(arr) == 0:
                break
            else:
                arr.popleft()
    if len(arr) == 0:
        print('error')
    else:
        print(arr)
