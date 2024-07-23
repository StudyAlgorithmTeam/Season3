from collections import deque

T=int(input())  # 테스트 케이스 개수
p=list(input())   # 수행할 함수
n=int(input())  # 배열의 수 개수
l=list(input()) # 배열에 들어있는 정수가 주어짐
l2=deque()
for i in l:
    if i!='[' and i!=']' and i!=',':
        l2.append(int(i))

for i in p:
    if i=='R':
        l2.reverse()
    elif i=='D':
        l2.popleft()
