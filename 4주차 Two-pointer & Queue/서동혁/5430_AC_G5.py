from collections import deque

T = int(input()) # T <= 100

# O(T (P+N))
for _ in range(T):
    p = list(input()) # len(check) < 100,000
    N = int(input()) # N < 100,000

    is_reversed = True
    is_broke = False
    # O(N)
    my_list = deque(input().replace('[','').replace(']','').split(','))

    if N == 0:
        my_list = deque([])

    # O(P)
    for i in p:
        # O(1)
        if i == 'R':
            is_reversed = not is_reversed
        # O(1)
        elif i == 'D':
            if len(my_list) == 0:
                print("error")
                break

            # O(1)
            if is_reversed:
                my_list.popleft()
            else:
                my_list.pop()
    else:
        my_list = list(my_list)

        if len(my_list) == 0:
            print("[]")
        elif len(my_list) == 1:
            # O(N)
            print("[" + ",".join(my_list) + "]")
        elif is_reversed:
            # O(N)
            print("[" + ",".join(my_list) + "]")
        else:
            # O(N)
            print("[" + ",".join(my_list[::-1]) + "]")
'''
    s = 0
    e = N-1

    if N == 0:
        input()
        my_list = []
    elif N == 1:
        my_list = [int(input().replace('[','').replace(']',''))]
    else:
        my_list = list(input().replace('[','').replace(']','').split(','))
        my_list = list((int)*my_list)
        print(my_list)

'''