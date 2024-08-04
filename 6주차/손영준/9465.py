import sys
input = sys.stdin.readline

t = int(input())
# 결국 임의의 스티커(A) 한 장 떼면 그 임의의 스티커(A)의 대각선만 사용 가능하다.
for _ in range(t): #O(t)
    n = int(input())
    dp = []
    for _ in range(2): 
        dp.append(list(map(int,input().split())))
        
    if n>1: # n>1이라는 조건이 없어서 indexError 발생.
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    for i in range(2,n): #O(n)
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
        
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        print(max(dp[0][n-1], dp[1][n-1]))
    # 시간복잡도: O(n*t)? n = 100,000


'''
    dp[0][i] = max(dp[1][i-1], dp[1][i-2])+dp[0][i]
    dp[1][i] = max(dp[0][i-1], dp[0][i-2])+dp[1][i]
    i의 열에서 i-1열의 대각선 or i-2열의 대각선중 큰 값과 i열의 값을 더한게 최대가 된다.
'''
