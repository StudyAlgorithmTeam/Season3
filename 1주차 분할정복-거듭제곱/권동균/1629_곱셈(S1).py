import sys
input=sys.stdin.readline
a,b,c = map(int, input().split())

def gob(a,b,c):
    if b==1: return a%c
    elif b%2==0:
        return pow(gob(a%c, b//2, c),2)%c
    else:
        return pow(gob(a%c, b//2, c),2)*a%c
        
print(gob(a,b,c))
