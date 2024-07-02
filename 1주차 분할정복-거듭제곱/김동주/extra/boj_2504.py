# 괄호의 값


PAIR = {
    ')': '(',
    ']': '[',
}
VALUE = {
    ')': 2,
    ']': 3,
}


def solve(s: str) -> int:
    stack = []

    def calc_inner_value() -> int:
        """(X) 혹은 [X]의 상황에서 X의 가치를 구함."""
        inner_value = 0
        while stack and isinstance(stack[-1], int):
            inner_value += stack.pop()
        return max(inner_value, 1)

    for c in s:
        # 열리는 괄호면 스택에 넣고 넘김
        if c in '([':
            stack.append(c)
            continue
        # 닫히는 괄호면 괄호열의 가치를 계산한다.
        inner_value = calc_inner_value()
        # 괄호 쌍에서 괄호의 종류가 일치하는지 검사
        if not stack or stack.pop() != PAIR[c]:
            return 0
        stack.append(VALUE[c]*inner_value)
    value = calc_inner_value()
    if stack:
        # 아직 덜 닫힌 괄호들이 존재
        return 0
    return value


if __name__ == "__main__":
    print(solve(input().strip()))
