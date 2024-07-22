import ast
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

result = []

for i in range(T):
    count = 0
    p_arr = list(input())
    p = int(input())
    str_list = input()
    arr = deque(ast.literal_eval(str_list))    
    for i in p_arr:
        if i == 'R':
            arr.reverse()
        elif i == 'D':
            if len(arr) > 0:    
                arr.popleft()
            else:
                count = 1
                break
                
    if count == 1:
        result.append("error")
    else:
        result.append(list(arr))
    
print(*result,sep="\n")