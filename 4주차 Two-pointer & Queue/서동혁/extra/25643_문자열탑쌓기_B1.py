N, M = map(int,input().split())

temp_list = []

for i in range(N):
    temp_list.append(list(input()))

ex = temp_list[0]
count = 0

for items in temp_list:
    next = items
    check = 0

    for j in range(1,M+1):
        if ex[0:j] == next[M-j::]:
            check = 1
            break
        elif ex[M-j::] == next[0:j]:
            check = 1
            break
    ex = next

    if check:
        count += 1
    else:
        print(0)
        break
    if check and count == N:
        print(1)
