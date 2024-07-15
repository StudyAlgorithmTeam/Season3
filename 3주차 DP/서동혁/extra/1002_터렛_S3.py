import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if length == 0:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    elif length == (r1+r2):
        print(1)
    elif length > (r1+r2):
        print(0)
    elif length < (r1+r2):
        if length + min(r1,r2) == max(r1,r2):
            print(1)
        elif length + min(r1,r2) < max(r1,r2):
            print(0)
        else:
            print(2)