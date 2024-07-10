# 엔비스카의 영혼


N, a, b = map(int, input().split())

F = list(range(2*N+1))

for i in range(N+1):
    F[i] = min(F[i], F[i-a-1]+1)
    F[i] = min(F[i], F[i-b-1]+1)

print(F[N])
