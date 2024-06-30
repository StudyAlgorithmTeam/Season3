# 수열의 가치

from collections import Counter


N = int(input())
A = list(map(int, input().split()))

max_value = 0
max_b = []
counter = Counter(A)
numbers = sorted(counter)
for mid in numbers:
    p = []
    q = []
    value = mid * counter[mid]
    for num in numbers:
        value += num * counter[num]
        if num < mid:
            p = p + [num] * counter[num]
        else:
            q = [num] * counter[num] + q
    b = p + q
    if max_value < value:
        max_value = value
        max_b = b

print(max_value)
print(*max_b)
