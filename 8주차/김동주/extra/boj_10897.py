# Inherited disease


MOD = int(1e9+7)

D, *d = map(int, open(0).read().split())


FACTORIAL = [1] * (D+1)
for i in range(1, D+1):
    FACTORIAL[i] = (FACTORIAL[i-1] * i) % MOD


def traverse():
    row = 1  # 이전 세대의 노드의 개수
    col = 1  # 동 세대에서 몇 번째 노드인지.
    for i in range(D):
        col = ((i+1)*(col-1) + d[i]) % MOD
        yield (row + col - 1) % MOD
        row = (row + FACTORIAL[i+1]) % MOD


print('\n'.join(map(str, traverse())))
