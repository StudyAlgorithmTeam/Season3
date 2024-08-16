# 전깃줄

import sys
from typing import List, Set


class SegmentTree:
    # binary tree for range queries

    def __init__(self, n: int, default=0) -> None:
        self.tree = [default] * (4*n)
        self.n = n

    def __op__(self, left: int, right: int) -> int:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f'<SegmentTree top={self.top()}>'

    def top(self) -> int:
        return self.tree[1]

    def update(self, i: int, value: int) -> None:
        node = self.get_node(i)
        self.tree[node] = value
        while node > 1:
            parent = node//2
            self.tree[parent] = self.__op__(
                self.tree[2*parent],
                self.tree[2*parent+1],
            )
            node = parent

    def get_node(self, i: int) -> int:
        s, e = 0, self.n-1
        node = 1
        while s < e:
            mid = (s+e)//2
            if mid >= i:  # go to left node
                e = mid
                node = 2*node
            else:  # go to right node
                s = mid+1
                node = 2*node+1
        return node


A = 0
B = 1

N = int(sys.stdin.readline())
CABLES = []

for u in range(N):
    a, b = map(int, sys.stdin.readline().split())
    CABLES.append((a, b))


# 전깃줄간 교차 여부에 대한 그래프. 각 노드는 전깃줄이다.
G: List[Set[int]] = [set() for _ in range(N)]

for u in range(N):
    for v in range(u):
        # 두 전깃줄이 교차하려면, 양 끝 점의 상하 관계가 반대이면 됨.
        if (CABLES[u][A] - CABLES[v][A]) * (CABLES[u][B] - CABLES[v][B]) < 0:
            G[u].add(v)
            G[v].add(u)


class RangeSumTree(SegmentTree):
    def __op__(self, left: int, right: int) -> int:
        return left + right


class RangeMaxIndexTree(SegmentTree):
    def __op__(self, left: int, right: int) -> int:
        if len(G[left]) > len(G[right]):
            return left
        else:
            return right


range_sum_tree = RangeSumTree(N)
range_max_idx_tree = RangeMaxIndexTree(N)


for u in range(N):
    range_sum_tree.update(u, len(G[u]))
    range_max_idx_tree.update(u, u)


removed_count = 0

while range_sum_tree.top():
    u = range_max_idx_tree.top()  # 제거할 노드 선택 (가장 많은 교차점을 가진 것)
    for v in G[u]:
        G[v].remove(u)
        range_sum_tree.update(v, len(G[v]))
        range_max_idx_tree.update(v, v)
    G[u].clear()
    range_sum_tree.update(u, len(G[u]))
    range_max_idx_tree.update(u, u)

    removed_count += 1

print(removed_count)
