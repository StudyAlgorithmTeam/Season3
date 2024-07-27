# Alice and Bob

import math


def solve(n: int, c: list) -> str:
    """
    >>> solve(2, [2, 3])
    'Alice'
    >>> solve(2, [5, 3])
    'Alice'
    >>> solve(3, [5, 6, 7])
    'Bob'
    >>> solve(3, [2, 4, 8])
    'Alice'
    >>> solve(3, [1, 4, 8])
    'Alice'
    >>> solve(3, [2, 4, 9])
    'Bob'
    >>> solve(2, [13, 31])
    'Alice'
    >>> solve(2, [1, 2])
    'Bob'
    >>> solve(2, [3, 9])
    'Alice'
    >>> solve(2, [3, 9, 27])
    'Alice'
    """
    return "Alice" if can_alice_win(n, c) else "Bob"


def can_alice_win(n: int, c: list) -> bool:
    # O(N^2 log max(c))
    """
    서로소가 있을 경우(coprime) 어떻게든 1을 만들어 모든 숫자를 만들어 낼 수 있다.
    그런 경우가 있는지를 찾는다.

    GCD는 유클리드 알고리즘을 기준으로 시간복잡도를 계산한다:
    O(number of bits) = O(log N)
    """

    # 모든 숫자가 특정 수의 배수이면, 해당 수보다 작은 수는 만들 수 없고,
    # 만드는 모든 수 또한 그 수의 배수가 된다.
    # 전역 GCD를 구하여 이를 보정해주자.

    # O(N log max(c))
    gcd = math.gcd(*c)
    # O(N)
    for i in range(n):
        c[i] //= gcd

    # O(N^2 log max(c))
    for i in range(n):
        for j in range(i):
            # O(log max(c))
            if math.gcd(c[i], c[j]) == 1:
                # 이 부분은 딱 1번만 실행되므로
                # 전체 시간복잡도에 +N 만 해주면 되지만
                # 최고차항이 이미 N을 초과하므로 무시.
                return (max(c)-n) % 2 == 1
    return False


if __name__ == "__main__":
    n = int(input())
    # O(n)
    c = [*map(int, input().split())]
    # O(n^2 log max(c))
    print(solve(n, c))
