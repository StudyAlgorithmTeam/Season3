import sys
import collections

for t in range(int(sys.stdin.readline())):
    P = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    # deque = collections.deque(eval(sys.stdin.readline()))
    deque = collections.deque(sys.stdin.readline().strip()[1:-1].split(','))
    is_reversed = False
    if deque[0] == '':
        deque.popleft()
    for p in P:
        match p:
            case 'R':
                is_reversed = not is_reversed
            case 'D':
                if not deque:
                    print('error')
                    break
                if is_reversed:
                    deque.pop()
                else:
                    deque.popleft()
    else:
        arr = list(deque)
        if is_reversed:
            arr.reverse()
        sys.stdout.write('['+','.join(arr)+']\n')
