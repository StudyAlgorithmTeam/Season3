C, N = map(int, input().split())
# C <= 1000, N <= 20

city = []

for i in range(N):
    city.append(list(map(int, input().split())))

max_value = max(city,key=lambda x:x[1])[1]

DP = [100001] * (C + max_value + 1)
DP[0] = 0

for x in city: # O( N*(C+100) )
    weight = x[0]
    customer = x[1]

    for i in range(customer, C + max_value + 1):
        DP[i] = min(DP[i], DP[i-customer] + weight)

print(min(DP[C:]))