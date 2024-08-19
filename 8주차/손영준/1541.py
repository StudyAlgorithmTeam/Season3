arr = input().split('-') #O(n), n = 입력 문자열 최대 길이
'''
가장 처음숫자와 마지막 숫자는 숫자가 된다. -> 처음부터 부호가 올 일은 없음.
'-'를 기준으로 나눌 때, if 입력이 "10+20-30+40-50", arr는 ['10+20', '30+40', '50']이 된다
주어진 입력 최대값: 50
'''
res = 0

for i in arr[0].split('+'): #res는 30이 된다.
    res += int(i)
for i in range(1,len(arr)):
    for j in arr[i].split('+'): 
        res -= int(j)
'''
나머지 요소도 처리해준다. 각 요소를 +를 기준으로 해서 나눠주고 각 값을 빼준다.
예를 들면, arr[1] ='30+40'이고, arr[2] = '50'이 되면서 각각 반복문 차례에서 빼준다.
각 반복문마다 입력 문자열 최대 길이만큼만 확인하니까 O(n)..? O(n^2)..?
'''
print(res)
