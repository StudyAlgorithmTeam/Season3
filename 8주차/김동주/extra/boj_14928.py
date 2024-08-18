MOD = 20000303
N = 0
for c in input().strip():
    N = (10*N + int(c)) % MOD
print(N)
