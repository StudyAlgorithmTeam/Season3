# 겹치는 건 싫어

import collections


def solve(N: int, K: int, A: list) -> int:
    """
    >>> solve(9, 2, [3, 2, 5, 5, 6, 4, 4, 5, 7])
    7
    >>> solve(10, 1, [1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
    6
    """
    max_len = 0

    # 지금 내가 보고 있는 수열의 구간
    queue = collections.deque()

    # 지금 내가 보고 있는 수열에서 각 숫자별 등장 횟수
    counter = collections.Counter()

    for i in range(N):
        while counter[A[i]] >= K:
            counter[queue[0]] -= 1
            queue.popleft()
        counter[A[i]] += 1
        queue.append(A[i])
        max_len = max(max_len, len(queue))

    return max_len


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = [*map(int, input().split())]
    print(solve(N, K, A))
