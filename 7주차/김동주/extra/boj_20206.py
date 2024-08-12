# 푸앙이가 길을 건너간 이유


A, B, C = map(int, input().split())
X1, X2, Y1, Y2 = map(int, input().split())


def f(x: int) -> int:
    return -(A*x+C)/B


def f_inv(y: int) -> int:
    return -(B*y+C)/A


def is_poor():
    if A == 0:
        y = -C/B
        return Y1 < y < Y2
    if B == 0:
        x = -C/A
        return X1 < x < X2
    return X1 < f_inv(Y1) < X2 or X1 < f_inv(Y2) < X2 or (Y1 < f(X1) < Y2) or (Y1 < f(X2) < Y2)



if is_poor():
    print('Poor')
else:
    print('Lucky')
