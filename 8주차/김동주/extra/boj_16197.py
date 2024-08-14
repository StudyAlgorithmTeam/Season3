# 두 동전

from collections import deque
import sys


class AnswerFound(Exception):
    pass


MAX_MOVES = 10

DX = [-1, 0, 0, 1]
DY = [0, -1, 1, 0]

N, M = map(int, sys.stdin.readline().split())

is_wall = [[False] * M for y in range(N)]

# 두 공의 좌표가 (y1, x1, y2, x2) 형태로 들어갈 예정.
balls = []
for y in range(N):
    for x, val in enumerate(sys.stdin.readline().strip()):
        if val == '#':
            is_wall[y][x] = True
        elif val == 'o':
            balls.append(y)
            balls.append(x)

try:
    queue = deque([balls])
    for moves in range(1, MAX_MOVES+1):
        for _ in range(len(queue)):
            cy1, cx1, cy2, cx2 = queue.popleft()
            for dy, dx in zip(DY, DX):
                ny1, nx1, ny2, nx2 = cy1+dy, cx1+dx, cy2+dy, cx2+dx

                # 공이 떨어졌는지 여부
                is_on_board_1 = (0 <= ny1 < N and 0 <= nx1 < M)
                is_on_board_2 = (0 <= ny2 < N and 0 <= nx2 < M)

                if (not is_on_board_1) and (not is_on_board_2):
                    # 두 공 중에 하나만 떨어뜨린 것이 아님.
                    continue

                if (not is_on_board_1) or (not is_on_board_2):
                    # 정답을 찾은 경우. GOTO문 (혹은 return문) 처럼 사용하기
                    raise AnswerFound

                # 두 공이 모두 보드 위에 있는 경우.
                if is_wall[ny1][nx1]:
                    ny1, nx1 = cy1, cx1
                if is_wall[ny2][nx2]:
                    ny2, nx2 = cy2, cx2
                queue.append([ny1, nx1, ny2, nx2])
except AnswerFound:
    print(moves)
else:
    print('-1')
