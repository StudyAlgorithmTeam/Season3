MOD_NUM = 1000000007
A = [[1, 1], [1, 0]]

def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j]) % MOD_NUM
    return temp

def matrix_pow(n, M):
    if n == 1:
        return M
    temp = matrix_pow(n//2, M)
    if n % 2 == 0:
       return matrix_mult(temp, temp)
    else:
        return matrix_mult(matrix_mult(temp,temp), M)

print(matrix_pow(int(input()), A)[0][1] % MOD_NUM)