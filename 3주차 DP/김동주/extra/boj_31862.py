# 승리하라

import collections
import sys


class RangeMaxTree:
    def __init__(self, n: int, not_counted=[]):
        self.n = n
        self.tree = [0] * (4*n)
        self.not_counted = not_counted

    def top(self) -> int:
        return self.tree[1]

    def get(self, i: int) -> int:
        return self.tree[self._index(i)]

    def query(self, lo: int, hi: int) -> int:
        return self._query(1, 0, self.n-1, lo, hi)

    def _query(self, node: int, start: int, end: int, lo: int, hi: int) -> int:
        if hi < start or end < lo:
            return 0
        if lo <= start and end <= hi:
            return self.tree[node]
        mid = (start+end)//2
        return max(
            self._query(node*2, start, mid, lo, hi),
            self._query(node*2+1, mid+1, end, lo, hi),
        )

    def update(self, i: int, value: int):
        node = self._index(i)
        self.tree[node] = value
        if i in self.not_counted: # 개조된 구간 트리이다.
            return
        while (node := node//2):
            self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])

    def _index(self, i: int) -> int:
        s, e = 0, self.n-1
        node = 1
        while s < e:
            mid = (s+e)//2
            if i <= mid:
                e = mid
                node *= 2
            else:
                s = mid+1
                node = node*2+1
        return node


if __name__ == "__main__":
    MAX_N = int(2e5)
    N, M, K = map(int, sys.stdin.readline().split())

    # 이 구간 트리는 K번 팀을 제외한 팀들의 점수중 최댓값을 저장한다.
    tree = RangeMaxTree(MAX_N+1, not_counted=[K])

    game_counter = collections.Counter()

    for i in range(M):
        t1, t2, r = map(int, sys.stdin.readline().split())
        if r == 1:
            tree.update(t1, tree.get(t1)+1)
            continue
        if r == 2:
            tree.update(t2, tree.get(t2)+1)
            continue
        game_counter[(t1, t2)] += 1
    games = [(t1, t2, game_counter[(t1, t2)]) for t1, t2 in game_counter]

    def bruteforce(i: int) -> int:
        if i == 0:
            # 2등 보다는 점수가 커야 유일한 1등이다.
            return 1 if tree.get(K) > tree.top() else 0
        cases = 0
        t1, t2, count = games[i-1]
        for c in range(count+1):
            tree.update(t1, tree.get(t1)+c)
            tree.update(t2, tree.get(t2)+count-c)
            cases += bruteforce(i-1)
            tree.update(t1, tree.get(t1)-c)
            tree.update(t2, tree.get(t2)-count+c)
        return cases

    print(bruteforce(len(games)))
