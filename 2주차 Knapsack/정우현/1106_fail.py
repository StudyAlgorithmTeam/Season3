C,N = map(int,input().split())
arr_mony = []
arr_piple =[]

for i in range(N):
    a,b = map(int,input().split())
    arr_mony.append(a)
    arr_piple.append(b)

result = []

def minmony(i,mony):
    if i >= C:
        result.append(mony)
    if i == N:
        i = 0
    return max(arr_piple[i] + minmony(i+1, mony + arr_mony[i]), minmony(i+1,mony), arr_mony[i] + minmony(i, mony+arr_mony[i]))



minmony(0,0)
result.sort()
print(result[0])

#넣는다. 안넣는다. 현재를 넣는다.
#그리고 비용과 값을 같이 넣어서 비용이 가장 작은 것을 넣는다. 