MOD = 1000000007

def Div(arr):
    ans = [[0, 0], [0, 0]]
    ans[0][0] = arr[0][0] % MOD
    ans[0][1] = arr[0][1] % MOD
    ans[1][0] = arr[1][0] % MOD
    ans[1][1] = arr[1][1] % MOD
    return ans

def Mul(arr1, arr2):
    ans = [[0, 0], [0, 0]]
    ans[0][0] = (arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0]) % MOD
    ans[0][1] = (arr1[0][0] * arr2[0][1] + arr1[0][1] * arr2[1][1]) % MOD
    ans[1][0] = (arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0]) % MOD
    ans[1][1] = (arr1[1][0] * arr2[1][0] + arr1[1][1] * arr2[1][1]) % MOD
    return ans

def pow(a, b):
    if b == 1:
        return Div(a)
    
    i = pow(a, b // 2)
    if b % 2 == 0:
        return Div(Mul(i, i))
    else:
        return Div(Mul(Div(Mul(i, i)), a))

def main():
    n = int(input())
    a = [[1, 1], [1, 0]]
    
    result = pow(a, n)
    print(result[0][1])
    return

main()
