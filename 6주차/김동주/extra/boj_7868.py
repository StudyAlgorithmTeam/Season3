# 해밍 수열

import math


MAX = int(1e18)

*p, i = map(int, input().split())
p.sort()

hammings = []
for p1 in range(int(math.log(MAX, p[0]))+1):
    for p2 in range(int(math.log(MAX, p[1]))+1):
        for p3 in range(int(math.log(MAX, p[2]))+1):
            hammings.append(p[0]**p1 * p[1]**p2 * p[2]**p3)
hammings.sort()

# hammings[0]은 1이지만, 이는 해밍 수열의 첫번째 수가 아님. 어쩌다 보니 제로패딩이 된 꼴.
print(hammings[i])
