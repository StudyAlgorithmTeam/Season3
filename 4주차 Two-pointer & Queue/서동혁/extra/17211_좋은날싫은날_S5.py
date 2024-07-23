N, mood = map(int,input().split())
mood_list = list(map(float,input().split()))

good = [0] * 101
bad = [0] * 101

if mood:
    bad[0] = 1
else:
    good[0] = 1
for i in range(1,N+1):
    good[i] = good[i-1] * mood_list[0] + bad[i-1] * mood_list[2]
    bad[i] = bad[i-1] * mood_list[3] + good[i-1] * mood_list[1]

print(round(good[N] * 1000))
print(round(bad[N] * 1000))