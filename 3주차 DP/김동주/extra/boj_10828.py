# 스택

import sys


stack = []
ops = {
    'push': stack.append,
    'pop': lambda: sys.stdout.write(f'{stack.pop() if stack else -1}\n'),
    'size': lambda: sys.stdout.write(f'{len(stack)}\n'),
    'empty': lambda: sys.stdout.write(f'{0 if stack else 1}\n'),
    'top': lambda: sys.stdout.write(f'{stack[-1] if stack else -1}\n'),
}

N = int(sys.stdin.readline())
for i in range(N):
    cmd, *arg = sys.stdin.readline().split()
    ops[cmd](*arg)
