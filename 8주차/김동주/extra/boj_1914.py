# 하노이 탑

from sys import stdout
from typing import List, Tuple


class TowerOfHanoiSimulator:
    def __init__(self, n: int, src: int, dst: int) -> None:
        assert n > 0
        assert src != dst
        self.n = n
        self.src = src
        self.dst = dst

    def simulate(self):
        raise NotImplementedError

    def get_move_count(self) -> int:
        raise NotImplementedError

    def list_move_histories(self) -> List[Tuple[int, int]]:
        raise NotImplementedError


class _HistorySimulator(TowerOfHanoiSimulator):
    def __init__(self, n: int, src: int, dst: int) -> None:
        super().__init__(n, src, dst)
        self.move_history = []

    def simulate(self) -> int:
        self._move(self.n, self.src, self.dst)
        return len(self.move_history)

    def _move(self, n: int, src: int, dst: int):
        if n > 0:
            other = 6-src-dst
            self._move(n-1, src, other)
            self.move_history.append((src, dst))
            self._move(n-1, other, dst)

    def get_move_count(self) -> int:
        return len(self.move_history)

    def list_move_histories(self) -> List[int]:
        return self.move_history


class _CountOnlySimulator(TowerOfHanoiSimulator):
    def __init__(self, n: int, src: int, dst: int) -> None:
        super().__init__(n, src, dst)
        self.cache = {0: 0}
        self.move_count = 0

    def simulate(self) -> int:
        self.move_count = self._cached_move(self.n)
        return self.move_count

    def _cached_move(self, n: int) -> int:
        # 기록을 안 해도 되면 옮길 수 있는지 여부만 알아도 충분하다.
        if n not in self.cache:
            self.cache[n] = 2 * self._cached_move(n-1) + 1
        return self.cache[n]

    def get_move_count(self) -> int:
        return self.move_count

    def list_move_histories(self) -> List[int]:
        return []


def get_toh_simulator(n: int) -> TowerOfHanoiSimulator:
    if n > 20:
        return _CountOnlySimulator(n, 1, 3)
    else:
        return _HistorySimulator(n, 1, 3)


if __name__ == "__main__":
    N = int(input())
    toh = get_toh_simulator(N)
    toh.simulate()
    stdout.write(f'{toh.get_move_count()}\n')
    for src, dst in toh.list_move_histories():
        stdout.write(f'{src} {dst}\n')
