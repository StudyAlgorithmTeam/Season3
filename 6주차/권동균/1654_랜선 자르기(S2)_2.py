import sys
input=sys.stdin.readline

# O(1)
K, N=map(int,input().split())

# O(K)
l=[int(input()) for _ in range(K)]

start=1
end=max(l)
result=0

def binary(start, end, l):
    global result
    cnt=0
    if start>end:
        return
    else:
        mid=(start+end)//2
        for i in l:
            cnt+=i//mid
        
        if cnt < N:
            end=mid-1
        else:
            result=mid
            start=mid+1
        return binary(start, end, l)
        
binary(start, end, l)
print(result)
