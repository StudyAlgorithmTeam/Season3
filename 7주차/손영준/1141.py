# 문제를 풀기 전 접두사를 체크하는 과정에서 작년 객프수업때 프로젝트 진행하면서 startsWith()라는 함수를 자바에서 사용한 적이 있었는데 파이썬에도 있는지 찾아봤는데 진짜 있어서 사용해봤습니다.. 파이썬 짱짱맨.
# 자바에선 불리안 값으로 사용했는데 
n = int(input())
arr = []
cnt = 0
# 한 단어가 다른 단어의 접두사가 되려면 보통 먼저 있는 접두사의 길이가 더 작아야한다. 접두사X인 부분집합을 확인하려면 입력받은 문자열들을 길이순으로 정렬한다.
# 한 단어는 본인보다 뒤에 위치한 문자와 비교하면 된다.
for _ in range(n):
    x = input()
    arr.append(x)
arr.sort(key=len)

for i in range(n):
    is_prefix = False
    for j in range(i+1,n): #i번째 일 때, i보다 한 칸 뒤에 위치한 문자부터 비교
        if arr[j].startswith(arr[i]):
            is_prefix = True
            break
        '''else:
            cnt += 1 
            처음엔 이렇게 했었는데 이렇게 하면 중복되는 경우가 생겨서 cnt값이 생각보다 많아진다.'''
    if not is_prefix:
        cnt += 1
        
print(cnt)
