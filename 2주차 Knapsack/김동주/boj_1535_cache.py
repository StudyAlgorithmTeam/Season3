# 안녕


N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

INF = max(J)+1


cache = {}


def max_joy(i = 0, life = 100) -> int:
    key = (i, life)
    if key not in cache:
        if life <= 0:
            # 절대 수복 못할 절망을 맛보게 하자.
            cache[key] = -INF
        elif i == N:
            # 모든 사람을 다 본 경우
            cache[key] = 0
        else:
            cache[key] = max(
                J[i] + max_joy(i+1, life-L[i]), # 인사하는 경우
                max_joy(i+1, life), # 인사하지 않는 경우
            )
    return cache[key]


print(max_joy())
