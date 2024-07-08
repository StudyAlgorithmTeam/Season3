N = int(input()) # 사람 수
L = list(map(int, input().split())) # 체력 잃기
J = list(map(int, input().split())) # 기쁨 얻기

def max_joy(i,l):
    if l<=0: return -1000000000 # 죽음
    elif l>0 and i==N: # 모든 사람 다 돌았을 경우
        return 0
    else:
        # 인사 X - max_joy(i+1, l)          
        # 인사 O - max_joy(i+1, l-L[i])+J[i]
        return max(max_joy(i+1, l), max_joy(i+1, l-L[i])+J[i])
      
        # 인사 O일때 남은 체력바 고려 - (l-L[i])
        # -> 통과 시 더 기뻐지기 - (+J[i])

# 0번째 사람, 채력 100 시작
print(max_joy(0, 100))
