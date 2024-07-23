# 루트 게임

import sys


MAX_N = int(1e6)


def square_generator(hi: int):
    return map(lambda x: x*x, range(1, int(hi**0.5)+1))


# 점화식을 이용한 바텀업 DP
F = [False] * (MAX_N+1)

for n in square_generator(MAX_N):
    F[n] = True

for n in range(1, MAX_N+1):
    if F[n]:
        continue
    for x in square_generator(MAX_N-n):
        if not F[n+x]:
            F[n+x] = True


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        N = int(sys.stdin.readline())
        if F[N]:
            sys.stdout.write("koosaga\n")
        else:
            sys.stdout.write("cubelover\n")
