import math
T=int(input())

def d(x1, y1, x2, y2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int, input().split())

    dot_distance=d(x1,y1,x2,y2)
    rp=r1+r2
    rm=abs(r2-r1)

    if x1==x2 and y1==y2:
        if r1==r2: print(-1)
        else: print(0)

    else:
        if rp==dot_distance or rm==dot_distance: print(1)
        elif rp>dot_distance and rm<dot_distance: print(2)
        else: print(0)
