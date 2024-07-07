# 호텔

from functools import cache
import math
import sys


C, N = map(int, sys.stdin.readline().split())
group_cost = [None] * N
group_size = [None] * N
for i in range(N):
    group_cost[i], group_size[i] = map(int, sys.stdin.readline().split())


@cache
def find_min_price(i = 0, c = C) -> int:
    """i번째 도시부터 N번째 도시까지 적어도 c명의 고객을 유치하기 위해 투자해야할 최소 금액"""
    if c <= 0:
        # C명을 유치했으므로, 이제 더 비용을 안 소모해도 됨.
        return 0

    min_cost = sys.maxsize
    max_possible_groups = math.ceil(c / group_size[i]) # 적어도 c명을 유치하기 위해 투자해야 하는 최소 횟수

    if i == N-1:
        # i번째 도시가 마지막 도시이면 선택권이 없이 투자에 올인 해야한다.
        return max_possible_groups * group_cost[i]

    # 0 부터 max_possible_groups 번까지 투자해보면서 최소 비용을 찾는다.
    for n_groups in range(max_possible_groups+1):
        # i번째 도시에 n_groups 번 투자하는 경우:
        cost = find_min_price(i+1, c - n_groups * group_size[i]) + n_groups * group_cost[i]
        if min_cost > cost:
            min_cost = cost
    return min_cost


print(find_min_price())
