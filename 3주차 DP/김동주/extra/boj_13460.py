# 구슬 탈출 2

import collections
import sys


N, M = map(int, sys.stdin.readline().split())
IS_WALL = [[False] * N for x in range(M)]
R = 0, 0
B = 0, 0
O = 0, 0

for y in range(N):
    for x, cell in enumerate(sys.stdin.readline().strip()):
        if cell == "#":
            IS_WALL[x][y] = True
        elif cell == "R":
            R = x, y
        elif cell == "B":
            B = x, y
        elif cell == "O":
            O = x, y


def move_red(rx, ry, bx, by, dx, dy):
    while not IS_WALL[rx+dx][ry+dy] and (rx+dx, ry+dy) != (bx, by) and (rx, ry) != O:
        rx += dx
        ry += dy
    return rx, ry


def move_blue(rx, ry, bx, by, dx, dy):
    return move_red(bx, by, rx, ry, dx, dy)


def solve() -> int:
    q = collections.deque([(*R, *B)])
    visited = collections.defaultdict(lambda: False)
    for tries in range(10):
        for w in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if (rx, ry, bx, by) in visited:
                continue
            visited[(rx, ry, bx, by)] = True

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nrx, nry, nbx, nby = rx, ry, bx, by
                nrx, nry = move_red(nrx, nry, nbx, nby, dx, dy)
                nbx, nby = move_blue(nrx, nry, nbx, nby, dx, dy)
                nrx, nry = move_red(nrx, nry, nbx, nby, dx, dy)

                if (nbx, nby) == O:
                    continue

                if (nrx, nry) == O:
                    return tries+1

                q.append((nrx, nry, nbx, nby))
    return -1


if __name__ == "__main__":
    ans = solve()
    print(ans)
