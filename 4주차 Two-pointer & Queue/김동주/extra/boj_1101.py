# 카드 정리 1

from typing import List
import sys


# O(NM(N + log M))
def solve(N: int, M: int, B: List[List[int]]) -> int:
    """
    N: number of boxes
    M: number of colors

    >>> solve(3, 2, [[1, 1], [1, 1], [1, 0]])
    1
    >>> solve(2, 2, [[2, 0], [1, 1]])
    0
    >>> solve(4, 2, [[1, 0], [1, 0], [0, 1], [0, 1]])
    1
    >>> solve(6, 2, [[1, 1], [1, 1], [1, 1], [1, 0], [1, 0], [0, 1]])
    3
    >>> solve(11, 12, [[0, 2, 0, 0, 0, 8, 0, 0, 0, 0, 7, 0],
    ...                [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    ...                [0, 6, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    ...                [0, 0, 6, 0, 0, 0, 0, 0, 0, 3, 6, 2],
    ...                [0, 0, 0, 7, 2, 0, 0, 0, 0, 0, 0, 0],
    ...                [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    ...                [0, 0, 4, 0, 0, 9, 0, 0, 3, 0, 0, 0],
    ...                [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    ...                [0, 2, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0],
    ...                [0, 0, 0, 5, 0, 0, 2, 0, 0, 0, 0, 0],
    ...                [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]])
    6
    """
    boxes = []  # 상자 별로 색이 많은 순서대로 정렬된 색들의 리스트
    # O(NM log M)
    for box_id in range(N):
        # O(M)
        box = [color for color in range(M) if B[box_id][color] > 0]
        # O(M log M)
        box.sort(key=lambda color: B[box_id][color], reverse=True)
        boxes.append(box)

    global_min_moves = N

    # O(N^2 M)
    # 임의로 조커 박스를 하나 선정해본다
    for joker_box_id in range(N):
        local_min_moves = 0  # 최소 이동 횟수
        n_empty_boxes = 0  # 빈 상자의 개수

        box_id_of_color = [None] * M # 색상별로 상자를 지정한다.

        is_box_fixed = [False] * N # 각 상자별로 더 이상 카드를 이동시키지 않을지 여부
        is_box_fixed[joker_box_id] = True

        # O(N)
        # 우선 색상을 고정할 수 있는 경우 고정한다.
        for box_id in range(N):
            if is_box_fixed[box_id]:
                continue
            # 빈 상자의 개수는 미리 세어둔다.
            if len(boxes[box_id]) == 0:
                is_box_fixed[box_id] = True
                n_empty_boxes += 1
                continue
            # 색상이 하나 밖에 없는 경우, 선택된 상자를 해당 색상의 카드만 담는 상자로 지정한다.
            if len(boxes[box_id]) == 1:
                color = boxes[box_id][0]
                if box_id_of_color[color] is None:
                    box_id_of_color[color] = box_id
                    is_box_fixed[box_id] = True
                else:
                    # 이미 해당 색상을 담는 다른 박스가 있다면, 카드를 이동시켜준다.
                    local_min_moves += 1
                    is_box_fixed[box_id] = True

        # O(NM)
        # 나머지 상자들에 대해 색상을 고정한다.
        for box_id in range(N):
            if is_box_fixed[box_id]:
                continue

            # O(M)
            for color in boxes[box_id]:
                # 색상이 고정된 상자가 없다면, 색상을 고정한다.
                if not is_box_fixed[box_id] and not box_id_of_color[color]:
                    box_id_of_color[color] = box_id
                    is_box_fixed[box_id] = True
                    continue

                # 그 외의 경우엔, 색상별 상자, 혹은 조커 박스로 색상을 이동시켜야 한다.
                # 여러 색상이 있더라도 한 번에 이동시킬 것이므로, 다른 색상은 검사하지 않는다.
                local_min_moves += 1
                break

        if local_min_moves < global_min_moves:
            global_min_moves = local_min_moves

    return global_min_moves


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    B = [[*map(int, sys.stdin.readline().split())] for i in range(N)]
    print(solve(N, M, B))
