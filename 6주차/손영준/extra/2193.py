#DP 문제를 탐색하다가 쉽게 풀어버린 문제..:)
n = int(input())
dp = [0]*91 #문제에서 n이 최대 90개

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,n):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n-1])

'''
    1 = 1
    2 = 10
    3 = 100, 101
    4 = 1000, 1001, 1010
    5 = 10000, 10001, 10010, 10100, 10101
    6 = 100000, 100001, 100010, 100100, 101000, 101001, 101010, 100101
    규칙을 찾다보니 설마 피보나치..? -> 근데 맞음 
'''
