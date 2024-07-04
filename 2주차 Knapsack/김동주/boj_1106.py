# 호텔

from functools import cache
import math
import sys


C, N = map(int, sys.stdin.readline().split())
unit_price = [None] * N
unit_amount = [None] * N
for i in range(N):
    unit_price[i], unit_amount[i] = map(int, sys.stdin.readline().split())


@cache
def find_min_price(i = 0, c = C) -> int:
    """i번째 도시부터 N번째 도시까지 적어도 c명의 고객을 유치하기 위해 투자해야할 최소 금액"""
    if c <= 0:
        # C명을 유치했으므로, 이제 더 비용을 안 소모해도 됨.
        return 0

    min_price = sys.maxsize
    max_n_units = math.ceil(c / unit_amount[i]) # 적어도 c명을 유치하기 위해 투자해야 하는 최소 횟수

    if i == N-1:
        # i번째 도시가 마지막 도시이면 선택권이 없이 투자에 올인 해야한다.
        return max_n_units * unit_price[i]

    for n_units in range(max_n_units+1):
        price = find_min_price(i+1, c - n_units * unit_amount[i]) + n_units * unit_price[i]
        if min_price > price:
            min_price = price
    return min_price


print(find_min_price())
