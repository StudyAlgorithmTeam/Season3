x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2+x2*y3+x3*y1-(y1*x2+y2*x3+y3*x1)

op1=ccw(x1,y1,x2,y2,x3,y3)
op2=ccw(x1,y1,x2,y2,x4,y4)
op3=ccw(x3,y3,x4,y4,x1,y1)
op4=ccw(x3,y3,x4,y4,x2,y2)

if op1*op2<0 and op3*op4<0: print(1)
else: print(0)
