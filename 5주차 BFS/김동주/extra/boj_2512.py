# 예산


def cost(hi):  # O(N)
    """예산 상항액이 hi일때 필요한 총 예산"""
    return sum(min(x, hi) for x in X)


N = int(input())
X = [*map(int, input().split())]
M = int(input())

ans = 0

lo = 0
hi = min(M, max(X))  # O(N)
# O(N log M) parametric search
while lo <= hi:
    mid = (lo + hi) // 2
    # O(N)
    if cost(mid) <= M:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
