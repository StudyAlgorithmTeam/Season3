n = int(input())
arr = [0]*(n+1)

if n%2 == 1:
    print(0)
else:
    arr[2] = 3
    for i in range(4,n+1,2):
        arr[i] = arr[i-2]*3 + 2
        for j in range(0,i-2,2):
            arr[i] += arr[j]*2
    print(arr[n])
    


# 2=3
# 4=11, arr[2]*3 +2
# 6=41, arr[4]*3 + dp[2]*2 + 2
# 8=153..?, arr[6]*3 + dp[4]*2 + dp[2]*2 + 2
