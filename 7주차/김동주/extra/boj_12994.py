# 이동3-2


MAX_K = 32

K = [1]
for i in range(1, MAX_K):
    K.append(3*K[i-1])


def solve(x: int, y: int, k=0) -> bool:
    if x == 0 and y == 0:
        return True
    if x and (x+K[k]) % K[k+1] == 0:
        return solve(x+K[k], y, k+1)
    if x and (x-K[k]) % K[k+1] == 0:
        return solve(x-K[k], y, k+1)
    if y and (y+K[k]) % K[k+1] == 0:
        return solve(x, y+K[k], k+1)
    if y and (y-K[k]) % K[k+1] == 0:
        return solve(x, y-K[k], k+1)
    return False


if __name__ == "__main__":
    X, Y = map(int, input().split())
    print('1' if solve(X, Y) else '0')
