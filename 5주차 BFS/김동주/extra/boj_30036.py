# INK

import sys

# 플레이어가 조종하는 하얀 사각형의 위치
y = 0
x = 0

d = 0  # 점프 횟수
m = 0  # 잉크의 양




I, N, K = map(int, sys.stdin.readline().split())
C = sys.stdin.readline().strip().upper()
stage = [[None] * N for _ in range(N)]
for a in range(N):
    for b, cell in enumerate(sys.stdin.readline().strip()):
        # 사각형은 스테이지에서 잠시 제거
        if cell == '@':
            y = a
            x = b
            cell = '.'
        stage[a][b] = cell
for cmd in sys.stdin.readline().strip():
    match cmd:
        case 'U':
            if y-1 >= 0 and stage[y-1][x] == '.':
                y = y-1
        case 'D':
            if y+1 < N and stage[y+1][x] == '.':
                y = y+1
        case 'L':
            if x-1 >= 0 and stage[y][x-1] == '.':
                x = x-1
        case 'R':
            if x+1 < N and stage[y][x+1] == '.':
                x = x+1
        case 'j':  # 잉크 충전
            m += 1
        case 'J':  # 점프
            c_i = C[d % I]
            min_y = max(0, y-m)
            max_y = min(N-1, y+m)
            min_x = max(0, x-m)
            max_x = min(N-1, x+m)
            for a in range(min_y, max_y+1):
                for b in range(min_x, max_x+1):
                    if abs(y-a)+abs(x-b) > m:
                        continue
                    # 장애물이거나 이미 칠해져있다면.
                    if stage[a][b] == '#' or stage[a][b] in C:
                        stage[a][b] = c_i
            m = 0
            d += 1  # 점프 횟수 1 회 증가

# 제거했던 사각형을 다시 스테이지에 배치
stage[y][x] = '@'

# 스테이지 출력
sys.stdout.write('\n'.join(''.join(row) for row in stage))
