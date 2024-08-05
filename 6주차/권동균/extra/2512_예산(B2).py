N=int(input())
l=list(map(int, input().split()))
M=int(input())

start=1
end=max(l)

while start<=end:
    cnt=0
    mid=(start+end)//2

    for i in l:
        if mid>=i:  cnt+=i
        elif mid<i: cnt+=mid
    if cnt>M:
        end=mid-1
    else:   # cnt < M
        start=mid+1
print(end)
