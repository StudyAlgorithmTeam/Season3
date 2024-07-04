# 안녕

from functools import cache


N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

INF = max(J)+1


@cache
def max_joy(i = 0, life = 100) -> int:
    if life <= 0:
        # 절대 수복 못할 절망을 맛보게 하자.
        return -INF
    if i == N:
        # 모든 사람을 다 본 경우
        return 0

    return max(
        J[i] + max_joy(i+1, life-L[i]), # 인사하는 경우
        max_joy(i+1, life), # 인사하지 않는 경우
    )


print(max_joy())
