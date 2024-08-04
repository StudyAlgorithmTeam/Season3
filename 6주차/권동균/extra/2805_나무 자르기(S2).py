import sys
input=sys.stdin.readline
N, M=map(int, input().split())
l=list(map(int, input().split()))

start=1
end=max(l)

while start<=end:
    wood=0
    mid=(start+end)//2

    for i in l:
        if i>=mid:
            wood+=i-mid
    
    if wood<M:
        end=mid-1
    else:
        start=mid+1
print(end)
