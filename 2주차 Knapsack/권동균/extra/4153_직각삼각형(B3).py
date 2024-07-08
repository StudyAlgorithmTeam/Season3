def rt(x,y,z):
    if x*x+y*y==z*z or x*x+z*z==y*y or z*z+y*y==x*x:
        return 'right'
    else: return 'wrong'

while(1):
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else: print(rt(a,b,c))
