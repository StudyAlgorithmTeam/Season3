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