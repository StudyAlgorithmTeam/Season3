from collections import deque
import heapq

N, M = map(int,input().split())
my_list = list(map(int,input().split()))

count = [0] * 100001
dq = deque([])
tmp_max = []
my_max = 0

for tmp in my_list:
    dq.append(tmp)
    count[tmp] += 1
    my_max = my_max + 1

    if count[tmp] <= M:
        tmp_max.append(my_max)
    else:
        while(count[tmp]>M):
            count[dq.popleft()] -= 1
            my_max -= 1

print(max(tmp_max))

# counter = collections.Counter() 하면 숫자의 갯수를 알려줌