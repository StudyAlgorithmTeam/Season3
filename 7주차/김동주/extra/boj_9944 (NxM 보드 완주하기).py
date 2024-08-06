# NxM 보드 완주하기

from typing import List, Iterable, Tuple
import sys


MAX_CASES = int(1e6)

EMPTY = '.'
BLOCK = '*'

IMPOSSIBLE = -1

DX = (1, 0, 0, -1)
DY = (0, 1, -1, 0)


def solve(N: int, M: int, grid: List[List[str]]) -> int:
    """막혀있지 않은 모든 정점을 1번씩만 방문하는 최단경로의 길이.

    단, 모든 빈 칸을 방문할 수 없는 경우 -1을 반환한다.

    ---

    1. 격자 그래프에서 모든 정점의 수는 NxM이고, 정점의 수의 최댓값은 900이다.
    2. '가능한 이동 경로의 수는 1,000,000개를 넘지 않는다'는 전제가 존재한다.

    모든 정점에서 각각 완전탐색을 실시하면 최악의 경우, 900,000,000가지
    경우의 수가 존재할 것이다. 문제의 시간제한이 3초(Python은 30초)이므로
    (테스트 케이스의 개수가 많지 않다면) 가능한 풀이일 것으로 보인다.

    완전탐색은 백트래킹 기법을 이용한다.
    """
    def bruteforce() -> Iterable[int]:
        """모든 정점에 대해 백트래킹 수행

        모든 빈 칸을 방문할 수 없는 경우, sys.maxsize를 반환한다.
        """
        # O(V x (백트래킹 수행 시간))
        for y in range(N):
            for x in range(M):
                if grid[y][x] == EMPTY:
                    visit(y, x)
                    yield backtracking(y, x)
                    unvisit(y, x)

    def backtracking(y: int, x: int) -> int:
        """아직 방문하지 않은 모든 빈 칸을 방문하는 최단 경로의 길이를 구함.

        모든 빈 칸을 방문할 수 없는 경우, sys.maxsize를 반환한다.
        """
        nonlocal visited
        min_moves = sys.maxsize
        if n_not_visited == 0:
            # 모든 빈 칸을 방문함.
            min_moves = 0
        else:
            # 상하좌우로 주변의 방문하지 않은 빈 칸을 방문
            for dy, dx in zip(DY, DX):
                if not is_visitable(y+dy, x+dx):
                    continue
                ey, ex = do_move(y, x, dy, dx)
                moves = backtracking(ey, ex) + 1
                if min_moves > moves:
                    min_moves = moves
                undo_move(y, x, ey, ex, dy, dx)
        return min_moves

    # do_move()와 undo_move()에서 dx, dy는 방향을 표시하기 위한 수단임.

    def do_move(sy: int, sx: int, dy: int, dx: int) -> Tuple[int, int]:
        """도착 좌표(y,x)를 반환한다."""
        ex = sx
        ey = sy
        while is_visitable(ey+dy, ex+dx):
            ey += dy
            ex += dx
            visit(ey, ex)
        return ey, ex

    def undo_move(sy: int, sx: int, ey: int, ex: int, dy: int, dx: int) -> None:
        while ex != sx or ey != sy:
            unvisit(ey, ex)
            ey -= dy
            ex -= dx

    def visit(y: int, x: int):
        nonlocal n_not_visited
        visited[y][x] = True
        n_not_visited -= 1

    def unvisit(y: int, x: int):
        nonlocal n_not_visited
        visited[y][x] = False
        n_not_visited += 1

    def is_visitable(y: int, x: int) -> bool:
        return bool(
            (0 <= y < N) and
            (0 <= x < M) and
            not visited[y][x] and
            grid[y][x] == EMPTY
        )

    visited = [[True]*M for y in range(N)]
    n_not_visited = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == EMPTY:
                visited[y][x] = False
                n_not_visited += 1

    min_dist = min(bruteforce())
    return min_dist if (min_dist != sys.maxsize) else IMPOSSIBLE


if __name__ == "__main__":
    sys.setrecursionlimit(MAX_CASES)
    n_cases = 0
    while (line := sys.stdin.readline()):
        n_cases += 1
        N, M = map(int, line.split())
        grid = [sys.stdin.readline() for _ in range(N)]
        sys.stdout.write(f"Case {n_cases}: {solve(N, M, grid)}\n")
