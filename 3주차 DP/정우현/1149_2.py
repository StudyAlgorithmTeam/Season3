N = int(input())

r_arr = [0]
g_arr = [0]
b_arr = [0]

for i in range(N):
    r,g,b = map(int,input().split())
    r_arr.append(r)
    g_arr.append(g)
    b_arr.append(b)

dp_r = [0]*(N+1)
dp_g = [0]*(N+1)
dp_b = [0]*(N+1)

for i in range(1,N+1):
    dp_r[i] = min(dp_g[i-1],dp_b[i-1]) + r_arr[i]
    dp_g[i] = min(dp_r[i-1],dp_b[i-1]) + g_arr[i]
    dp_b[i] = min(dp_g[i-1],dp_r[i-1]) + b_arr[i]


print(min(dp_r[N],dp_g[N],dp_b[N]))
