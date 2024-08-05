# 청정수열 (Easy)

import math

N = int(input())

# 점수가 최소인 청정수열: 모든 동일한 숫자가 붙어있는 것.
# 숫자 쌍의 배치 순서가 관건이다.

print(math.perm(N))
