n=int(input())


if n%2 != 0: print(0)
elif n==2: print(3)
else:
    dp=[0]*(n+1)
    dp[2]=3

    for i in range(4,n+1,2):
        sum=0
        for j in range(0,i,2):
            sum+=dp[j]
        dp[i]=dp[i-2]*3+2+sum

    print(dp[n])
