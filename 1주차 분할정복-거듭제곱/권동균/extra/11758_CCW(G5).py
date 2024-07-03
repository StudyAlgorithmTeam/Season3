x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2+x2*y3+x3*y1-(y1*x2+y2*x3+y3*x1)

op=ccw(x1,y1,x2,y2,x3,y3)

if op<0: print(-1)
elif op>0: print(1)
else: print(0)
