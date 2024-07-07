def exp_by_sq(base: int, exp: int, mod: int) -> int:
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod
    if exp == 2:
        return (base * base) % mod
    y = exp_by_sq(exp_by_sq(base, exp // 2, mod), 2, mod)
    if exp % 2 == 1:
        y = (y * base) % mod
    return y


if __name__ == "__main__":
    A = int(input())
    X = int(input())
    MOD = int(1e9+7)
    print(exp_by_sq(A, X, MOD))
