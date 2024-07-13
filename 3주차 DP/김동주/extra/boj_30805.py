# 사전 순 최대 공통 부분 수열


def last_common_sequence(A, B):
    """사전 순 가장 나중인 공통 부분 수열을 찾는다."""
    # 먼저 가장 큰 수부터 찾아야 한다.
    # 동일한 수가 여럿 있다면 먼저 나오는 수를 선택해야 한다.
    # 스택으로 활용할 것이므로 우선순위가 높은게 뒤로 가도록 정렬한다.
    def key(x):
        return (x[0], -x[1])
    a_stack = sorted([(x, i) for i, x in enumerate(A)], key=key)
    b_stack = sorted([(x, i) for i, x in enumerate(B)], key=key)
    ai_last = -1
    bi_last = -1
    while a_stack and b_stack:
        a, ai = a_stack[-1]
        b, bi = b_stack[-1]
        if ai < ai_last:
            a_stack.pop()
            continue
        if bi < bi_last:
            b_stack.pop()
            continue
        if a == b:
            yield a
            ai_last = ai
            bi_last = bi
        if a >= b:
            a_stack.pop()
        if a <= b:
            b_stack.pop()


if __name__ == "__main__":
    N = int(input())
    A = [*map(int, input().split())]
    M = int(input())
    B = [*map(int, input().split())]

    lcs = [*last_common_sequence(A, B)]

    print(len(lcs))
    if lcs:
        print(*lcs)
