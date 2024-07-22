from collections import deque

T = int(input()) # T <= 100

for _ in range(T):
    check = list(input()) # len(check) < 100,000
    N = int(input()) # N < 100,000

    front = True
    TestFinish = False
    my_list = deque(input().replace('[','').replace(']','').split(','))
    
    if N == 0:
        my_list = deque([])

    for i in check:
        if i == 'R':
            front = not front
        elif i == 'D':
            if len(my_list) == 0:
                TestFinish = True
                break
            
            if front:
                my_list.popleft()
            else:
                my_list.pop()
    
    my_list = list(my_list)

    if TestFinish:
        print("error")
    else:
        if len(my_list) == 0:
            print("[]")
        elif len(my_list) == 1:
            print("[" + ",".join(my_list) + "]")
        elif front:
            print("[" + ",".join(my_list) + "]")
        else:
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