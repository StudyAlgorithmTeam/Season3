# 소수 구하기

import sys


lo, hi = map(int, input().split())

sieve = [True] * (hi+1)
sieve[0] = False
sieve[1] = False

# O(N \log \log N)
for i in range(2, int(hi**0.5)+1):
    if sieve[i]:
        # O((N/i)-i)
        for j in range(i+i, hi+1, i):
            sieve[j] = False

# O(N-M) = O(N)
for i in range(lo, hi+1):
    if sieve[i]:
        sys.stdout.write(f'{i}\n')
