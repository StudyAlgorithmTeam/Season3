N, M = map(int,input().split())
# N <= 1,000,000, M <= 2,000,000,000

log = list(map(int,input().split()))

max_height = 0
s = 0
e = max(log)

while(s <= e):
    total = 0
    mid = (s+e)//2

    for i in log:
        if mid < i:
            total += i-mid
    
    if total == M:
        max_height = mid
        break
    elif total > M:
        max_height = mid
        s = mid + 1
    else:
        e = mid - 1
print(max_height)