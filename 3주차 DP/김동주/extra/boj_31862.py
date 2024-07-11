# 승리하라

import sys


N, M, K = map(int, sys.stdin.readline().split())

score = [0] * (N+1)
games = []
for i in range(M):
    t1, t2, r = map(int, sys.stdin.readline().split())
    if r == 1:
        score[t1] += 1
    elif r == 2:
        score[t2] += 1
    else:
        games.append((t1, t2))


def top_n_teams(iterable, how_many):
    return sorted(iterable, key=lambda t: -score[t])[:how_many]


def bruteforce():
    return _bruteforce(len(games), *top_n_teams(range(1, N+1), 2))


def _bruteforce(i: int, top_1: int, top_2: int) -> int:
    cases = 0
    if i == 0:
        if (top_1 == K) and (score[top_1] > score[top_2]):
            cases += 1
    else:
        for t in games[i-1]:
            score[t] += 1
            cases += _bruteforce(i-1, *top_n_teams(set([t, top_1, top_2]), 2))
            score[t] -= 1
    return cases


print(bruteforce())
