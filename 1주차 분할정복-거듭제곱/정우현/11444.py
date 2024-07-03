def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    #2X2행렬 초기화한다
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] = (temp[i][j] + A[i][k] * B[k][j]) % 1000000007
    #3중 루프를 사용하여 두 행렬 A와 B를 곱한다.
    return temp
    #결과 행렬을 반환

def matrix_pow(n, M):
    if n == 1:
        return M
    if n % 2 == 0:
        temp = matrix_pow(n // 2, M)
        return matrix_mult(temp, temp)
    #홀수인 경우 1을 뺀 값을 추가해서 짝수로 만들어준다.
    else:
        temp = matrix_pow(n - 1, M)
        return matrix_mult(temp, M)


N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    A = [[1, 1], [1, 0]]
    result = matrix_pow(N - 1, A)
    print(result[0][0])
