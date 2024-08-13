'''
  문제를 풀기 전 접두사를 체크하는 과정에서 작년 객프수업때 프로젝트 진행하면서 startsWith()라는 함수를 자바에서 사용한 적이 있었는데,
  파이썬에도 있는지 찾아봤는데 진짜 있어서 사용해봤습니다.. 파이썬 짱짱맨.
  startswith() 함수는 O(l)입니다. 여기서 l은 문자열의 최대길이

  예제 3을보고 힌트를 얻어서 가장 작은 길이의 문자부터 차례대로 비교하는 방법을 사용했습니다.
'''

n = int(input())
arr = []
cnt = 0
# 한 단어가 다른 단어의 접두사가 되려면 보통 먼저 있는 접두사의 길이가 더 작아야한다. 접두사X인 부분집합을 확인하려면 입력받은 문자열들을 길이순으로 정렬한다.
# 한 단어는 본인보다 뒤에 위치한 문자와 비교하면 된다.
for _ in range(n): #O(n)
    x = input()
    arr.append(x)
arr.sort(key=len) #O(nlogn * l), l=문자열 최대길이(50)
#print(arr)

# 시간복잡도: 
for i in range(n): #O(n^2 * l), 이중for문
    is_prefix = False #만약 접두사라면 true, 접두사가 아니라면 false로 cnt를 증가시킨다.
    for j in range(i+1,n): #i번째 일 때, i보다 한 칸 뒤에 위치한 문자부터 비교
        if arr[j].startswith(arr[i]): #arr[i]가 arr[j]의 접두사인 경우
            is_prefix = True
            break
        '''else:
            cnt += 1 
            처음엔 이렇게 했었는데 이렇게 하면 한 번의 비교로 else문에 걸리면
            바로 걸려서 올바른 값이 나오지 않음. -> cnt값이 생각보다 많아진다.'''
    if not is_prefix:
        cnt += 1
        
print(cnt)

#전체 시간복잡도: O(n^2 * l) == 약 125,000, 시간제한은 2초이기 때문에 적절함. 
#n의 최대:50, l의 최대:50
