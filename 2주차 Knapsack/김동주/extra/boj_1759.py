import sys


L, C = map(int, input().split())
CHAR = sorted(input().split())


def make(i: int = 0, stack=[], vowels: int = 0):
    if len(stack) > L:
        return
    if i == len(CHAR):
        if len(stack) == L and vowels >= 1 and L - vowels >= 2:
            sys.stdout.write(''.join(stack)+'\n')
        return

    stack.append(CHAR[i])
    if CHAR[i] in 'aeiou':
        make(i+1, stack, vowels+1)
    else:
        make(i+1, stack, vowels)
    stack.pop()
    make(i+1, stack, vowels)


if __name__ == "__main__":
    make()
