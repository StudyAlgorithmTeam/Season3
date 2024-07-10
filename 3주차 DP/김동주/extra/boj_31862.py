# 승리하라

import sys


MAX_N = int(2e5)

N, M, K = map(int, sys.stdin.readline().split())


# 각 팀별 확정된 점수와, 아직 진행되지 않은 게임 파악
scores = [0] * (N+1)
unmatched = []
for team in range(M):
    t1, t2, r = map(int, sys.stdin.readline().split())
    match r:
        case 0:
            unmatched.append((t1, t2))
        case 1:
            scores[t1] += 1
        case 2:
            scores[t2] += 1


# U = 아직 진행되지 않은 게임의 개수
# U는 최대 20. (문제에 명시) -> O(2^U)에 완전탐색이 가능
U = len(unmatched)


# 구간 최댓값 트리를 이용해 최댓값을 log N에 갱신하고 조회하기
st = [0] * (4*MAX_N)


def st_index_of(team: int) -> int:
    """team의 인덱스를 구간 최댓값 트리에서 찾는다."""
    s, e = 0, MAX_N
    node = 1
    while s < e:
        m = (s+e)//2
        if m < team:
            node = node*2+1
            s = m+1
        else:
            node = node*2
            e = m
    return node


def st_update(team: int):
    """team의 점수가 갱신되었을 때, 구간 최댓값 트리를 갱신한다."""
    node = st_index_of(team)
    while (node := node//2) > 0:
        l, r = st[node*2], st[node*2+1]
        st[node] = l if scores[l] > scores[r] else r


# 구간 트리 초기화
st_offset = st_index_of(0)
for team in range(1, N+1):
    st[st_offset+team] = team
    st_update(team)


def st_first_max() -> int:
    """최댓값을 가지고 있는 팀을 반환한다."""
    return st[1]


def st_second_max() -> int:
    """두 번째로 큰 값을 가지고 있는 팀을 반환한다."""
    pri = st[1]
    pri_score = scores[pri]
    scores[pri] = -1
    st_update(pri)
    sec = st[1]
    scores[pri] = pri_score
    st_update(pri)
    return sec


def is_winner(team: int) -> bool:
    """team이 최댓값을 가지고 있는 유일한 팀인지 확인한다. (O(log N))"""
    if team != st_first_max():
        return False
    if scores[team] == scores[st_second_max()]:
        return False
    return True


def backtracking(i: int) -> int:
    if i == U:
        return 1 if is_winner(K) else 0
    cases = 0
    for t in unmatched[i]:
        scores[t] += 1
        st_update(t)
        cases += backtracking(i+1)
        scores[t] -= 1
        st_update(t)
    return cases


print(backtracking(0))
