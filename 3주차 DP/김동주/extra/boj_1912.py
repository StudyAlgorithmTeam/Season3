# 연속합


import functools


N = int(input())
A = [*map(int, input().split())]


@functools.cache
def f(i: int) -> int:
    """[0..i : i] 구간의 최대 연속합."""
    if i == 0:
        return A[0]
    return max(
        f(i-1)+A[i], # 이전 구간에서 이어지는 경우
        A[i], # i번째 수부터 구간을 새로 시작하는 경우
    )


print(max(f(i) for i in range(N)))
