# 크로스워드 퍼즐

import sys


def solve(M: int, N: int, U: int, L: int, R: int, D: int, puzzle: list) -> int:
    W = L+R+N
    H = U+D+M
    grid = [['.' if (y+x) % 2 else '#' for x in range(W)] for y in range(H)]
    for y in range(M):
        for x in range(N):
            grid[y+U][x+L] = puzzle[y][x]
    return '\n'.join(''.join(row) for row in grid)


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    U, L, R, D = map(int, sys.stdin.readline().split())
    puzzle = sys.stdin.read().strip().splitlines()
    print(solve(M, N, U, L, R, D, puzzle))
