# 두 박스

x1_min, y1_min, x1_max, y1_max = map(int, input().split())
x2_min, y2_min, x2_max, y2_max = map(int, input().split())


def classify() -> str:
    # 겹치는 구간의 사각형 좌표
    x_min = max(x1_min, x2_min)
    x_max = min(x1_max, x2_max)
    y_min = max(y1_min, y2_min)
    y_max = min(y1_max, y2_max)

    # 면적의 너비를 구하여 판별
    area = (x_max-x_min) * (y_max-y_min)

    if x_min > x_max or y_min > y_max:
        return 'NULL'
    elif area > 0:
        return 'FACE'
    elif x_min == x_max and y_min == y_max:
        return 'POINT'
    else:
        return 'LINE'


print(classify())
