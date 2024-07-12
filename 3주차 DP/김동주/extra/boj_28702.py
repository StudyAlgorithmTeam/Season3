# 웰컴 키트

import math


N = int(input())
SIZE = map(int, input().split())
T, P = map(int, input().split())

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지
print(sum(math.ceil(s/T) for s in SIZE))

# 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와,
# 그 때 펜을 한 자루씩 몇 개 주문하는지
print(N//P, N%P)