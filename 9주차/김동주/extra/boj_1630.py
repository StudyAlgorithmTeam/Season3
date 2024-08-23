# 오민식

from math import log

MOD = 987654321


def primes_lte(n: int):
    # sieve of eratosthenes
    # O(n log log n)
    sieve = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    for i in range(2, n+1):
        if sieve[i]:
            yield i


def mul(a: int, b: int, mod: int = MOD) -> int:
    # multiply with modulo
    return ((a % mod) * (b % mod)) % mod


def pow(base: int, exp: int, mod: int = MOD) -> int:
    # power with modulo, divide and conquer approach.
    # O(log exp)
    if exp == 0:
        return 1
    p = pow(base, exp//2, mod)
    p = mul(p, p, mod)
    if exp & 1:
        p = mul(p, base, mod)
    return p


def solve(N: int) -> int:
    lcm = 1
    for base in primes_lte(N):
        exp = int(log(N, base)) # O(log N)
        lcm = mul(lcm, pow(base, exp)) # O(log exp) = O(log log N)
    return lcm


if __name__ == "__main__":
    N = int(input())
    print(solve(N))
