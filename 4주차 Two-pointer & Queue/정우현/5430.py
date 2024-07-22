import ast
#문자 타입으로 입력된 list를 진짜 list로 바꾸기 위해 사용
from collections import deque

T = int(input())

result = []

for i in range(T):
    p_arr = list(input()) #명령어 배열
    p = int(input())
    
    str_list = input()
    if p == 0:
        arr = deque()
    else:
        arr = deque(ast.literal_eval(str_list))
        # literal_eval를 사용한다. class를 list로 바꿔줌
        
    count = 0 #error 발생 유무를 확인하기 위해 사용, 1이면 error
    R_ck = 0 #뒤집혔는지 확인하기 위해 사용 1이면 뒤집힌거고 0이면 그대로
      
    for i in p_arr:
        if i == 'R':
            if R_ck == 0: #뒤집힌지 여부 확인 반대로 만들어준다.
                R_ck += 1
            elif R_ck == 1:
                R_ck -= 1
        elif i == 'D':
            if arr:
                if R_ck == 0: #그대로면 왼쪽에서 하나를 지운다.    
                    arr.popleft()
                elif R_ck == 1:#뒤집혀 있으면 뒤에서 하나를 지운다.
                    arr.pop()
            else: #배열에 원소가 없는데 삭제하려 했으면 error
                count = 1
                break
                
    if count == 1:
        result.append("error")
    else:
        if R_ck == 1: #뒤집혀 있다고 판단되면 뒤집어준다.
            arr.reverse()
        result.append(f"[{','.join(map(str, arr))}]")
        #리스트에서 [1, 2]를 [1,2]로 바꿔주고 deque를 없애기 위해 사용
print(*result,sep="\n")

#시간 복잡도
#T번 반복, 명령어 길이 만큼 반복 -> p, reverse()는 O(N) 여기서 N은 P, 배열에 하나씩 넣어주는 것도 p, deque에서 popleft와 pop은 O(1)
#따라서 T*p + 2p인데 -> O(Tp)  . 


