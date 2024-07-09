T = int(input())

def dp(i,N):
    if i > N:
        return 0
    elif i == N:
        return 1
    elif i < N:
        return dp(i+1,N) + dp(i+2,N) + dp(i+3,N)

for i in range(T):
    temp = int(input())
    print(dp(0,temp))
    
'''
dp(0,4) = dp(1,4) + dp(2,4) + dp(3,4)

dp(1,4) = dp(2,4) + dp(3,4) + dp(4,4) = 4

dp(2,4) = dp(3,4) + dp(4,4) + dp(5,4) = 2

dp(3,4) = dp(4,4) + dp(5,4) + dp(6,4) = 1 '''
