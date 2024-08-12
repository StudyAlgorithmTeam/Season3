# N : 전체 용액의 수
N=int(input())

l=list(map(int, input().split()))

start=0
end=N-1
cnt=abs(l[start]+l[end])
S=start
E=end

# O(N)
while start<end:
    if abs(l[start]+l[end])<cnt:
        S=start
        E=end
        cnt=abs(l[start]+l[end])
    
    if l[start]+l[end]<0:
        start+=1
    elif l[start]+l[end]>0:
        end-=1
    else:
        break

print(l[S], l[E])


# O(N)
