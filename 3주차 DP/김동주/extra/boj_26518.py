# 수열의 극한값

b, c, a1, a2 = map(int, input().split())

N = int(1e4)

for n in range(3, N):
    an = b*a2 + c*a1
    a2, a1 = an, a2

print(a2/a1)
