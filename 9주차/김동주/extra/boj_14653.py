# 너의 이름은

import sys
import collections


N, K, Q = map(int, sys.stdin.readline().split())
MSG = []
for i in range(K):
    R, P = sys.stdin.readline().split()
    MSG.append([R, P])

if MSG[Q-1][0] == '0':
    # 모두 읽은 경우.
    sys.stdout.write('-1')
else:
    # 기본값이 False인 딕셔너리
    has_read = collections.defaultdict(bool)

    # 메시지를 역순으로 조회하며 읽은 사람들을 체크한다.
    i = K-1
    while i >= Q-1:
        has_read[MSG[i][1]] = True
        i -= 1

    # 연속한 이전 메시지들의 읽은 사람의 수가 변하지 않았으면
    # 읽은 사람들의 조합도 동일한 것이므로 포함시켜준다.
    while K-1 > i >= 0 and MSG[i][0] == MSG[i+1][0]:
        has_read[MSG[i][1]] = True
        i -= 1

    # 문제에서 '나'는 항상 모든 메시지를 읽는다고 함.
    has_read['A'] = True

    # 확정적으로 읽지 않은 사람들의 이름을 출력한다.
    for i in range(N):
        P = chr(ord('A')+i)
        if not has_read[P]:
            sys.stdout.write(P+' ')

sys.stdout.write('\n')
