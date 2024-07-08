# 타일 채우기

from functools import cache


@cache
def tile(n: int, *is_filled: bool) -> int:
    if n == 0:
        return 1 if all(is_filled) else 0
    match is_filled:
        case (False, False, False):
            return tile(n-1, True, True, True)
        case (False, False, True):
            return tile(n-1, True, True, False)
        case (False, True, False):
            return tile(n-1, True, False, True)
        case (False, True, True):
            return tile(n-1, True, False, False) + tile(n-1, True, True, True)
        case (True, False, False):
            return tile(n-1, False, True, True)
        case (True, False, True):
            return tile(n-1, False, True, False)
        case (True, True, False):
            return tile(n-1, False, False, True) + tile(n-1, True, True, True)
        case (True, True, True):
            return tile(n-1, True, True, False) + tile(n-1, False, True, True) + tile(n-1, False, False, False)


if __name__ == "__main__":
    N = int(input())
    print(tile(N, True, True, True))
