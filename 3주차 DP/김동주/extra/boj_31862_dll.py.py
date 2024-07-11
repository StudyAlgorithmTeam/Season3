# 승리하라

from __future__ import annotations
import dataclasses
import sys
import typing


@dataclasses.dataclass
class Node:
    key: int
    value: int
    prev: typing.Optional[Node] = None
    next: typing.Optional[Node] = None

    def __lt__(self, node: Node):
        return self.value < node.value

    def __repr__(self) -> str:
        return f"<{self.key}: {self.value}>"


class OrderedDoublyLinkedList:
    def __init__(self):
        self._node: typing.Dict[int, Node[int]] = {}
        self._head = None

    def __repr__(self) -> str:
        nodes = []
        node = self._head
        while node is not None:
            nodes.append(repr(node))
            node = node.next
        return " -> ".join(nodes)

    def __setitem__(self, key, value: int):
        node = self.get_node(key)
        node.value = value
        self._sift_prev(node)
        self._sift_next(node)

    def __getitem__(self, key) -> int:
        return self.get_node(key).value

    def get_node(self, key: int) -> Node:
        node = self._node.get(key, None)
        if node is None:
            node = self._create_node(key)
            self._insert_head(node)
        return node

    def _create_node(self, key: int) -> Node:
        node = Node(key, 0)
        self._node[key] = node
        return node

    def _insert_head(self, node: Node):
        if self._head is not None:
            node.next = self._head
            self._head.prev = node
        self._head = node

    def _sift_prev(self, node: Node):
        while (prev := node.prev) is not None and (node < prev):
            head = prev.prev
            next = node.next
            #       [head]->prev
            # head<-[prev]->node
            # prev<-[node]->next
            # node<-[next]

            node.prev, node.next = head, prev
            prev.prev, prev.next = node, next
            #       [head]->prev
            # head<-[node]->prev *
            # node<-[prev]->next *
            # node<-[next]

            if head is not None:
                head.next = node
            if next is not None:
                next.prev = prev
            #       [head]->node *
            # head<-[node]->prev
            # node<-[prev]->next
            # prev<-[next]       *
        if node.prev is None:
            self._head = node

    def _sift_next(self, node: Node):
        while (next := node.next) is not None and (next < node):
            prev = node.prev
            tail = next.next
            #       [prev]->node
            # prev<-[node]->next
            # node<-[next]->tail
            # next<-[tail]

            next.prev, next.next = prev, node
            node.prev, node.next = next, tail
            #       [prev]->node
            # prev<-[next]->node *
            # next<-[node]->tail *
            # next<-[tail]

            if prev is not None:
                prev.next = next
            if tail is not None:
                tail.prev = node
            #       [prev]->next *
            # prev<-[next]->node
            # next<-[node]->tail
            # node<-[tail]       *


if __name__ == "__main__":
    MAX_N = int(2e5)
    N, M, K = map(int, sys.stdin.readline().split())

    linked_list = OrderedDoublyLinkedList()

    games = []
    for i in range(M):
        t1, t2, r = map(int, sys.stdin.readline().split())
        if r == 1:
            linked_list[t1] += 1
        elif r == 2:
            linked_list[t2] += 1
        else:
            games.append((t1, t2))

    k_node = linked_list.get_node(K)

    def bruteforce(i: int) -> int:
        n_cases = 0
        if i == 0:
            # 1등이면서 2등 보다는 점수가 커야 유일한 1등이다.
            if (k_node.next is None) and (k_node.prev is None or k_node.value > k_node.prev.value):
                n_cases += 1
        else:
            for r in (0, 1):
                linked_list[games[i-1][r]] += 1
                n_cases += bruteforce(i-1)
                linked_list[games[i-1][r]] -= 1
        return n_cases

    print(bruteforce(len(games)))
