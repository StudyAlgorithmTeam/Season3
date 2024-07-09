# 추월

from collections import deque
import sys


N = int(sys.stdin.readline())

# 터널은 사실상 FIFO 구조.
tunnel = deque()
overspeeded_cars = set()

# 터널에 들어가는 차량을 Queue에 넣음
for i in range(N):
    car = sys.stdin.readline().strip()
    tunnel.append(car)

# 터널에서 나온 차량을 Queue에서 제거해가며 비교
for i in range(N):
    # 터널에서 나온 차량
    car = sys.stdin.readline().strip()

    # 이미 터널을 나왔던 (과속) 차량들은 Queue에서 제거
    while tunnel[0] in overspeeded_cars:
        tunnel.popleft()

    if tunnel[0] == car:
        tunnel.popleft()
    else:
        # 나와야 할 순서대로 나온 것이 아닌 경우 = 추월한 경우
        overspeeded_cars.add(car)

print(len(overspeeded_cars))
