# 폰 호석만


def solve(raw_input: str) -> str:
    """
    >>> solve('ep jh')
    '473 32 24'

    >>> solve('z z')
    'Impossible'

    >>> solve('0 0')
    'Multiple'

    >>> solve('2222222222222222222222222222222222222222222222222222222222222222222222 8888888888888888888888888888888')
    'Impossible'
    """
    cases = 0
    A = None
    B = None
    X = None
    A_num, B_num = raw_input.split()
    for A_base in range(2, 36+1):
        for B_base in range(2, 36+1):
            try:
                assert A_base != B_base
                if parse_int(A_num, base=A_base) == parse_int(B_num, base=B_base):
                    X = int(A_num, base=A_base)
                    A = A_base
                    B = B_base
                    cases += 1
            except (AssertionError, ValueError):
                pass
    if cases == 0:
        return "Impossible"
    elif cases == 1:
        return f"{X} {A} {B}"
    else:
        return "Multiple"


def parse_int(raw_number: str, base: int) -> int:
    """
    >>> parse_int("a", 16)
    10
    >>> parse_int("z", 36)
    35
    >>> parse_int("zz", 36)
    1295
    """
    number = 0
    for c in raw_number.lower():
        if c.isdigit():
            digit = int(c)
        else:
            digit = ord(c) - ord('a') + 10
        if digit >= base:
            raise ValueError
        number = number*base + digit
        if number > 1<<63:
            raise ValueError
    return number


if __name__ == "__main__":
    print(solve(input()))
