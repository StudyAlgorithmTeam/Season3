N = int(input())

r_arr = [0]
g_arr = [0]
b_arr = [0]

for i in range(N):
    r,g,b = map(int,input().split())
    r_arr.append(r)
    g_arr.append(g)
    b_arr.append(b)


def paintR(N):
    if N <= 0:
        return 0
    return min(paintB(N-1)+b_arr[N],paintG(N-1)+g_arr[N])


def paintG(N):
    if N <= 0:
        return 0
    return min(paintR(N-1)+r_arr[N],paintB(N-1)+b_arr[N])


def paintB(N):
    if N <= 0:
        return 0
    return min(paintR(N-1)+r_arr[N],paintG(N-1)+g_arr[N])

print(min(paintR(N),paintG(N),paintB(N)))
