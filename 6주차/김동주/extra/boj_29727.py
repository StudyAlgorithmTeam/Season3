# 선이 하나 더ㅠㅠ

# 이 풀이의 전반적인 시간복잡도는 math.comb(n, 2)의 시간복잡도에 선형 비례한다.

import math


def clamp(x: int, lo: int, hi: int) -> int:
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


n = int(input())
xa, ya = map(lambda x: float(x)+0.5, input().split())
xb, yb = map(lambda y: float(y)+0.5, input().split())

# 선분이 추가 되기 전, 만들 수 있는 모든 직사각형의 개수:
# (각 x,y 좌표에 대해 n+1개의 점중 2개를 고르면 됨.)
n_rect = math.comb(n+1, 2) * math.comb(n+1, 2)

# 변위
dy = ya-yb
dx = xa-xb

# y축에 평행한 경우
if dx == 0:
    # ny개 만큼 선택 가능한 점의 수가 늘었다.
    # 직선들은 0..n 구간에만 위치하므로 음수는 제외할 수 있도록 클램핑한다.
    max_y = clamp(math.floor(max(ya, yb)), 0, n)
    min_y = clamp(math.ceil(min(ya, yb)), 0, n)
    ny = max_y - min_y + 1

    # y좌표는 dy개의 점들 중 2개를 고르고,
    # x 좌표 중 하나는 x_a(=x_b)로 고정이므로
    # 나머지 x좌표 하나를 기존의 n+1개의 점들 중에 선택하면 된다.
    #
    # 만약 선택가능한 점의 수가 1개라면 새로운 직사각형은 만들 수 없다.
    # comb(1, 2) = 0 이므로, 아래의 수식만으로도 알아서 예외처리가 된다.
    n_rect += (n+1) * math.comb(ny, 2)

# x축에 평행한 경우 (y축에 평행한 경우와 유사)
if dy == 0:
    max_x = clamp(math.floor(max(xa, xb)), 0, n)
    min_x = clamp(math.ceil(min(xa, xb)), 0, n)
    nx = max_x - min_x + 1

    n_rect += math.comb(nx, 2) * (n+1)

print(n_rect)
