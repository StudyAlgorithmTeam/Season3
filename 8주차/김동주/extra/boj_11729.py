# 하노이 탑 이동 순서

import sys


def move(N: int, src=1, dst=3, moves=[]):
    if N == 0:
        return moves
    other = 6-src-dst
    move(N-1, src, other, moves)
    moves.append((src, dst))
    move(N-1, other, dst, moves)
    return moves


if __name__ == "__main__":
    N = int(input())
    moves = move(N)

    sys.stdout.write(f'{len(moves)}\n')
    for src, dst in moves:
        sys.stdout.write(f'{src} {dst}\n')
