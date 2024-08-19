from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int,input().split())
# N < 1000 , M < 500,000

dic = defaultdict(list)

for i in range(M):
    a,b = map(int,input().split())

    dic[a].append(b)
    dic[b].append(a)

check = [0] * (N+1)
check2 = [0] * (N+1)
count = 0

def dfs(root):
    check[root] = 1
        
    for i in dic[root]:
        if check[i] == 0:
            dfs(i)

def dfs_1(root):
    stack = [root]

    while stack:
        v = stack.pop()
        
        if check2[v] == 0:
            check2[v] = 1

            for i in dic[v]:
                stack.append(i)

for i in range(1,N+1):
    if check[i] == 0:
        count += 1
        dfs(i)

count2 = 0

for i in range(1,N+1):
    if check2[i] == 0:
        count2 += 1
        dfs_1(i)

print(count)
print(count2)
# 1 2 5 / 3 4 6