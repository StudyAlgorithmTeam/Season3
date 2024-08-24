# 가장 긴 증가하는 부분 수열 4

N = int(input())
A = [*map(int, input().split())]


# LIS propertise
size = [1] * N
link = [None] * N

# i -> j longest increasing subsequence
for i in reversed(range(N)):
    for j in reversed(range(i+1, N)):
        if A[i] < A[j] and size[i] < size[j]+1:
            size[i] = size[j] + 1
            link[i] = j


lis = []
i = size.index(max(size))
while i is not None:
    lis.append(A[i])
    i = link[i]

print(len(lis))
print(*lis)
