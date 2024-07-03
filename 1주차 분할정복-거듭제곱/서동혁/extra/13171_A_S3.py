MOD_NUM = 1000000007

def solution(A,X):
    if X == 1:
        return A % MOD_NUM

    temp = solution(A, X//2)

    if X % 2 == 1:
        return (temp * temp % MOD_NUM) * A % MOD_NUM
    else:
        return (temp * temp) % MOD_NUM

A = int(input())
X = int(input())

print(solution(A,X))