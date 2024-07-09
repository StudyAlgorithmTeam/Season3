n = int(input())
lost = list(map(int,input().split()))
get = list(map(int,input().split()))

best = []

for i in range(n):
    best.append((lost[i]/get[i], get[i], lost[i]))
    
best.sort()

health = 100
happy = 0

for i in range(n):
    if health - best[i][2] <= 0:
        continue
    
    health = health - best[i][2]
    happy = happy + best[i][1]

print(happy)

# 그리디로 했을 때 반례 ==> 그리디는 0/1 냅색은 불가능!
# 0일때도 zero division 에러 발생
# 6
# 59 49 18 94 5 70
# 45 62 12 15 99 28