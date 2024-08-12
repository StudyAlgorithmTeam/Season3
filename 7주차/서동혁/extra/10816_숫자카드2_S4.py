import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
N_Card = list(map(int,input().split())) # O(N)

M = int(input())
M_Card = list(map(int,input().split())) # O(M)
# N, M < 500,000

# 시간복잡도가 O(N + M) -> 약 100만인데 왜 시간초가 964ms 가 나오지??

dic = defaultdict(int)

for i in N_Card: # O(N)
    dic[i] += 1

for i in M_Card: # O(M)
    print(dic[i], end = ' ')

# https://dongdongfather.tistory.com/70
# counter 모듈도 있네

# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10816-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%EC%8B%A4%EB%B2%844-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89
# 이분탐색을 이렇게 사용하는데 dictionary는 O(1)이니 이렇게 찾을 필요가 없지 않나?