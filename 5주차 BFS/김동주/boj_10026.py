# 적록색약

from collections import deque
from typing import List
import sys


def traverse(grid: List[List[str]], visited: List[List[bool]], y: int, x: int):
    # BFS, O(V+E) = O(N^2)
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y+dy, x+dx
            if bool(
                0 <= ny < N and
                0 <= nx < N and
                grid[ny][nx] == grid[y][x] and
                not visited[ny][nx]
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    # O(N^2)
    grid_rb = [[None] * N for _ in range(N)]
    grid_rgb = [[None] * N for _ in range(N)]
    for y in range(N):
        for x, rgb in enumerate(sys.stdin.readline().strip()):
            grid_rgb[y][x] = grid_rb[y][x] = rgb
            # 적록색맹 세계관은 R이나 G, 둘 중 하나로 통일
            if rgb == 'G':
                grid_rb[y][x] = 'R'
    visited_rb = [[False] * N for _ in range(N)]
    visited_rgb = [[False] * N for _ in range(N)]


    rgb_areas = 0
    rb_areas = 0
    # O(N^2)
    for y in range(N):
        for x in range(N):
            if not visited_rgb[y][x]:
                traverse(grid_rgb, visited_rgb, y, x)
                rgb_areas += 1
            if not visited_rb[y][x]:
                traverse(grid_rb, visited_rb, y, x)
                rb_areas += 1

    print(rgb_areas, rb_areas)
