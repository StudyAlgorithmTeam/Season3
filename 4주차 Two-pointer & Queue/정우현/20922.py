N, a = map(int, input().split())

check = [0] * 200001
#0으로 된 200001칸 짜리 배열로 숫자가 몇번 나왔는지 체크
arr = list(map(int, input().split()))
#수열이 들어오는 배열

end = 0
#end는 늦게 오는 부분
result = []
#중간중간 길이를 저장하는 배열

#front는 앞에서 먼저 가는 부분
for front in range(N):
    check[arr[front]] += 1
    
    #숫자가 나온 횟수가 a보다 많게 되면 end를 늘려가면서 숫자를 하나씩
    #빼면서 체크 수를 하나씩 줄인다 a보다 크지 않으면 배열을 빠져 나온다
    while check[arr[front]] > a:
        check[arr[end]] -= 1
        end += 1
    
    result.append(front - end + 1)
    #배열은 0부터 시작하므로 1을 더해준다

result.sort()
result.reverse()
#저장되 길이중 가장 큰 수를 출력한다.
print(result[0])

#시간복잡도
# N만큼 반복, while문에서 이전 값들을 확인하는데 최악의 경우 N-1번 확인
# sort는 nlogn, reverse는 n
# 따라서 N(N-1) + NlogN + N -> O(N^2)