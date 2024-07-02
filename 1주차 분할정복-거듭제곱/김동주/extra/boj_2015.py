# 수들의 합 4

from collections import Counter


N, K = map(int, input().split())
A = [*map(int, input().split())]

# prefix sum
prefix_sum = [*A]
for i in range(1, N):
    prefix_sum[i] += prefix_sum[i-1]

cases = 0
counter = Counter([0])
for j in range(N):
    k = prefix_sum[j] - K
    # prefix_sum[i] (0 <= i < j) 이 k 인 것의 개수를 구해야 한다.
    #
    # N은 최대 200,000이므로, prefix_sum[i] = k인 것의 개수를 찾는데
    # O(log N) 이하의 알고리즘을 사용해야 함.
    #
    # dict에 기반한 Counter는 set, get에 hash를 사용하므로, 평균적으로 O(1)이 걸린다.
    # https://wiki.python.org/moin/TimeComplexity
    cases += counter[k]
    counter[prefix_sum[j]] += 1

print(cases)
