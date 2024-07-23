# 전투의 신


def solve(N, A, PA, B, PB) -> int:
    """
    문제의 예제 입력 1:
    >>> solve(16,7,2,9,4)
    (8, 0)

    시간 초과를 유도하는 예제:
    >>> solve(3,1,1,5,4)
    (3, 0)

    그 외
    >>> solve(13,1,4,2,5)
    (0, 2)
    """
    # Greedy Approach (가성비가 좋은 것만 사기)
    # 더 가성비가 좋은 쪽이 A이도록 한다.
    if A/PA < B/PB:
        return solve(N, B, PB, A, PA)[::-1]
    max_x = N//PA
    N %= PA
    max_y = N//PB
    N %= PB

    # 단순 가성비 좋은 것만 구매해서는 최적해를 찾을 수 없는 경우의 처리
    x, y = max_x, max_y
    while N and x > 1:
        x -= 1
        N += PA
        y += N//PB
        N %= PB
        if A*x+B*y > A*max_x+B*max_y:
            max_x, max_y = x, y
    return max_x, max_y


if __name__ == "__main__":
    N = int(input())
    A, PA, B, PB = map(int, input().split())
    print(*solve(N, A, PA, B, PB))
