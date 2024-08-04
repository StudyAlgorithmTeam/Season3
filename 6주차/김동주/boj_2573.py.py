# 빙산

# 전체 시간 복잡도:
# O(V) = O(NM) (V = 정점의 개수)
# o(500 x 11V + 3V) ~= o(5,500V)
# max(V) = 300^2 이므로, 근사 수행시간 T를 구해보면
# T = 5,500 x 90,000 ~= 500,000,000
# 수행 시간 T가 5억에 가까우므로 시간초과의 가능성이 있다. 시간 제한이 타이트한 문제.


from collections import deque
import sys


DY = (0, 1, 0, -1)
DX = (1, 0, -1, 0)

MELTED = 0


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # O(V) = O(NM)
        # o(2V)
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
        # O(V+E) = O(V) = O(NM)
        # o(V+E) = o(V+4V) = o(5V)
        for y in range(self.height):
            for x in range(self.width):
                # 이 문제의 핵심:
                # 2개의 그리드 맵을 활용하여, 새 빙하의 값을 구하는 과정에서
                # 기존 빙하의 값에 영향을 안 주는 것.
                self.buffer[y][x] = self.grid[y][x]
                for ny, nx in self.neighbors_of(y, x):
                    # 하한은 0, 주변(상하좌우)에 완전히 녹은 영역의 개수만큼 감소.
                    if self.buffer[y][x] > 0 and self.grid[ny][nx] == MELTED:
                        self.buffer[y][x] -= 1
        self.grid, self.buffer = self.buffer, self.grid

    def count_areas(self) -> int:
        # O(V) = O(NM)
        # o(V+V+E) = o(V+V+4V) = o(6V)
        areas = 0
        # BFS를 위한 준비
        queue = deque()
        visited = self.buffer  # 공간 재활용
        # visited 초기화, O(V) = O(NM)
        for y in range(self.height):
            for x in range(self.width):
                visited[y][x] = self.grid[y][x] == MELTED
        # BFS를 이용한 영역 개수 세기 O(V+E) = O(V), o(V+E) = o(5V)
        # 모든 칸을 1회만 방문한다. O(V)
        # 각 칸 별로 모든 인접한 칸을 1회 검사한다: O(E) = O(4V)
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == MELTED:
                    continue
                if visited[y][x]:
                    continue
                # 새로운 영역 발견
                # -> 연결된 모든 칸을 방문처리함.
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

    # O(V)
    # o(2V)
    grid = Grid(width=M, height=N)

    # O(V)
    # o(V)
    for y in range(N):
        for x, ice in enumerate(map(int, sys.stdin.readline().split())):
            grid.grid[y][x] = ice

    # O(V) = O(NM)
    # o(500 x 11V)
    #
    # 루프 1회당 시간 복잡도: O(V) = O(MN), o(11V)
    #
    # 루프의 개수:
    # 최악의 경우 10,000칸의 빙산이 있을 수 있고, 모두 높이가 10인 경우
    # 100x100 격자로 빙산을 이룰때, 약 500번 루프를 돌 가능성이 있다.
    steps = 0
    while (areas := grid.count_areas()) == 1:
        grid.simulate()
        steps += 1

    if areas == 0:
        print(0)
    else:
        print(steps)
