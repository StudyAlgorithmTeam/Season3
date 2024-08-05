N=int(input())
lst=[]
for i in range(N):
    s,e=map(int, input().split())
    lst.append([s,e])

# 두 번째 값으로 정렬하는 법
lst.sort(key=lambda x:(x[1], x[0]))

cnt=1
end=lst[0][1]
for i in range(1, N):
    if lst[i][0] >= end:
        cnt+=1
        end=lst[i][1]

print(cnt)
