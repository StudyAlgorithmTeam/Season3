# Prime Tree - 1

from typing import List
from math import gcd
import sys


def solve(V_size: int, E: List[List[int]]) -> int:
    V_fix = set()
    V_map = {}  # reassigned map

    def reassign(u: int, v: int) -> bool:
        if V_map[v] not in V_fix:
            V_map[u], V_map[v] = V_map[v], V_map[u]
            return True
        return False

    def calc_R() -> float:
        # O(V+E)
        M = 0
        X = 0
        for u in range(1, V_size+1):
            for v in E[u]:
                M += 1
                if gcd(V_map[u], V_map[v]) > 1:
                    X += 1
        return X/M

    def backtracking(u: int) -> bool:
        # O(V!)
        if u > V_size:
            return calc_R() == 0
        for v in range(1, V_size+1):
            if reassign(u, v):
                V_fix.add(V_map[u])
                if backtracking(u + 1):
                    return True
                V_fix.remove(V_map[u])
        return False

    for i in range(1, V_size+1):
        V_map[i] = i
    backtracking(1)
    return [V_map[i] for i in range(1, V_size+1)]


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        E = [[] for _ in range(n+1)]
        for i in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            E[u].append(v)
            E[v].append(u)
        V = solve(n, E)
        sys.stdout.write(' '.join(map(str, V)) + '\n')
