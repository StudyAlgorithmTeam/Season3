# 괄호의 값


PAR_TYPE_MATCHER = {
    ')': '(',
    ']': '[',
}
PAR_VALUE_MULTIPLIER = {
    ')': 2,
    ']': 3,
}


def solve(s: str) -> int:
    stack = [[None, 0]] # (괄호의 종류, 괄호열 내부 값의 가치)
    try:
        for c in s:
            # 열리는 괄호면 스택에 넣고 넘김
            if c in '([':
                stack.append([c, 0])
                continue

            # 닫히는 괄호면 괄호열의 가치를 계산한다.
            assert len(stack) > 0
            par_type, inner_value = stack.pop()

            # 괄호 쌍에서 괄호의 종류가 일치하는지 검사
            assert par_type == PAR_TYPE_MATCHER[c]

            # 부모 괄호열 내부 값의 가치에, 현재 괄호열의 가치를 더함
            stack[-1][1] += max(inner_value, 1) * PAR_VALUE_MULTIPLIER[c]

        assert len(stack) > 0
        par_type, value = stack.pop()

        # 모든 괄호열 쌍이 매칭되어 스택을 초기화 할 때 삽입했던 노드만 남아있어야 함.
        assert par_type is None
        return value

    except AssertionError:
        return 0


if __name__ == "__main__":
    print(solve(input().strip()))
