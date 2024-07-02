import sys
input = sys.stdin.readline

n = int(input())
matrix = [[1,1], [1,0]]

def matmul(mat1,mat2):
    result = [[0]*2 for _ in range(2)] #2차원 배열~
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= 1000000007
    #for 3중문으로 행렬곱 구현~
    return result

def dq(a,b):
    if b == 1:
        return a
    powNum = dq(a,b//2)
    powNum = matmul(powNum,powNum)  #b가 짝수일땐 그냥 진행
    if b % 2 != 0: #b가 홀수
        powNum = matmul(powNum,a)
    return powNum

if n == 0:
    print(0)
else:
    resultAll = dq(matrix, n)
    print(resultAll[0][1])
