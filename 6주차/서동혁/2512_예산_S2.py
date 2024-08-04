N = int(input())
# 3 <= N <= 10,000
budget = list(map(int,input().split())) # O(N)
# budget 원소값 < 100,000

M = int(input())

s = 1
e = max(budget)
result = 0 # 결과값(mid)

# O( N * log(max(budget)))
if sum(budget) <= M: 
    result = max(budget)
else:
    while(s <= e): # O(log2Max(budget)) -> O(log100,000)
        total = 0
        mid = (s+e)//2

        for i in budget: # O(N)
            if i > mid:
                total += mid
            else:
                total += i
        
        if total == M:
            result = mid
            break
        elif total > M:
            e = mid - 1
        else:
            result = mid
            s = mid + 1

print(result)