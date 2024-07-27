# Alice and Bob

import sys


def solve(n: int, c: list) -> str:
    """
    >>> solve(2, [2, 3])
    'Alice'
    >>> solve(2, [5, 3])
    'Alice'
    >>> solve(3, [5, 6, 7])
    'Bob'
    """
    visited = set(c)
    if can_alice_win(c, visited):
        return "Alice"
    else:
        return "Bob"


def can_alice_win(c: list, visited: set) -> bool:
    for xi in reversed(range(len(c))):
        for yi in range(xi):
            z = abs(c[xi] - c[yi])
            if z in visited:
                continue
            visited.add(z)
            c.append(z)
            if not can_alice_win(c, visited):
                return True
            visited.remove(z)
            c.pop()
    return False


if __name__ == "__main__":
    sys.setrecursionlimit(int(1e6))
    n = int(input())
    c = [*map(int, input().split())]
    print(solve(n, c))
