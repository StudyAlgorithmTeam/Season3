# 검문

# 전체 시간복잡도:
# O(N log max(A) + sqrt(max(A) - min(A)) log sqrt(max(A) - min(A)))
# 이 때, max(A) = 1e9, min(A) = 1 이다.
# Big-O 노테이션에서 작은 수인 min(A)은 생략해도 무방해보이므로 정리하면,
# O(N log max(A) + sqrt(max(A)) log sqrt(max(A))) 이다.

# 사전에 구한 log 1e9 ~= 30, sqrt(1e9) ~= 31623, log sqrt(1e9) ~= 14 이다.
# 따라서, 시간복잡도는 대략 o(30 N + 31623*14) = O(N) 이다.

import sys
import math


N = int(sys.stdin.readline())

# O(N)
A = [*map(int, sys.stdin.readlines())]


# O(N log max(A))
# 1. 유클리디언 알고리즘 시간복잡도: O(log min(A))
# 2. 왜 max(A)인가?
#   -> 모든 A값을 보기에, 유클리디언 알고리즘에서 최악의 경우 O(log (A에서 2번째로 가장 큰 값)) 이 된다.
#   -> 2번째로 가장 큰 값을 편의상 max(A)로 근사하여 나타낸 것이다.
max_M = math.gcd(*[A[i]-A[i+1] for i in range(N-1)])


# O(sqrt(max(A) - min(A)))
# O(sqrt(max_M))
# -> max_M: A의 모든 원소들의 차이의 최대공약수.
# -> max_M = O(max(A) - min(A))
# M = (max_M의 약수 중 1을 제외한 것들의 집합)
M = [max_M]
for divisor in range(2, int(math.sqrt(max_M))+1):
    if max_M % divisor != 0:
        continue
    M.append(divisor)
    if max_M // divisor <= divisor:
        continue
    M.append(max_M // divisor)

# O(sqrt(max_M) log sqrt(max_M))
#
# len(M) = (max_M의 약수의 개수) 이다.
# 약수의 개수의 상한은 O(sqrt(max_M)) 이다.
# 따라서, len(M) = O(sqrt(max_M)) 이다.
M.sort()

# O(sqrt(max_M))
print(*M)
