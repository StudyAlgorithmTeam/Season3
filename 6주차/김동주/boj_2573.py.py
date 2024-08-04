# 빙산

from collections import deque, defaultdict
import sys


DY = (0, 1, 0, -1)
DX = (1, 0, -1, 0)

MELTED = 0


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # O(NM)
        self.grid = [[0]*width for _ in range(height)]
        self.buffer = [[0]*width for _ in range(height)]

    def is_in_bound(self, y: int, x: int) -> bool:
        return (0 <= y < self.height) and (0 <= x < self.width)

    def neighbors_of(self, y: int, x: int):
        # O(1)
        # o(4)
        for dy, dx in zip(DY, DX):
            if self.is_in_bound(y+dy, x+dx):
                yield y+dy, x+dx

    def simulate(self):
        # O(NM)
        # o(5NM) = O(V+E) = o(V+4V)
        for y in range(self.height):
            for x in range(self.width):
                self.buffer[y][x] = self.grid[y][x]
                for ny, nx in self.neighbors_of(y, x):
                    if self.buffer[y][x] > 0 and self.grid[ny][nx] == MELTED:
                        self.buffer[y][x] -= 1
        self.grid, self.buffer = self.buffer, self.grid

    def count_areas(self) -> int:
        # O(NM)
        # o(6NM) = o(V+V+E) = o(V+V+4V)
        areas = 0
        # BFS
        queue = deque()
        visited = self.buffer  # 공간 재활용
        for y in range(self.height):
            for x in range(self.width):
                visited[y][x] = self.grid[y][x] == MELTED
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == MELTED:
                    continue
                if visited[y][x]:
                    continue
                queue.append((y, x))
                visited[y][x] = True
                while queue:
                    for ny, nx in self.neighbors_of(*queue.popleft()):
                        if self.grid[ny][nx] == MELTED:
                            continue
                        if visited[ny][nx]:
                            continue
                        queue.append((ny, nx))
                        visited[ny][nx] = True
                areas += 1
        return areas


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    grid = Grid(width=M, height=N)
    for y in range(N):
        for x, ice in enumerate(map(int, sys.stdin.readline().split())):
            grid.grid[y][x] = ice

    # O(NM)
    # o(5500 NM) = o(5,500 * 90,000) ~= o(500,000,000)
    # 5억에 가까우므로 시간초과의 가능성이 있다.
    #
    # 루프 1회당 O(NM), o(11NM)
    # 최악의 경우 10,000칸의 빙산이 있을 수 있고, 모두 높이가 10인 경우
    # 100x100 격자로 빙산을 이룰때, 약 500년이 걸릴 수도 있다.
    steps = 0
    while (areas := grid.count_areas()) == 1:
        grid.simulate()
        steps += 1

    if areas == 0:
        print(0)
    else:
        print(steps)
