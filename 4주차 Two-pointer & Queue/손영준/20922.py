import sys
input=sys.stdin.readline

n,k = map(int,input().split()) #n: 배열길이, k:같은 숫자 나올 수 있는 최대 횟수
arr = list(map(int,input().split()))
cnt = 100001*[0] #해당 숫자가 몇 번 나왔는지 체크하는ㄴ 배열
start,end,result = 0,0,0 
#시작점, 끝점, 결과값

#시간복잡도:O(N)?
while end < n: #끝점이 n미만일 때까지만 반복한다
    if cnt[arr[end]] < k: #현재 숫자가 k번 미만으로 나오면~
        cnt[arr[end]] += 1 
        end += 1 #다음으로 점 이동
    else: #현재 숫자가 k번 이상 나오면
        cnt[arr[start]] -= 1 
        start +=1 #다음으로 점 이동      
        
    result = max(result,end -start) #while문 안에서 최대값 비교후 갱신
print(result)

'''
    먼저 start, end가 배열의 처음 부분을 가리키고, 여기서 start가 가리키는 숫자가 k개 미만 나오면 right를 증가시켜서 범위를 확장시킨다. 
    만약 start가 가리키는 숫자가 k개 이상 나온다면 start를 증가시켜서 범위를 줄인다.
'''
