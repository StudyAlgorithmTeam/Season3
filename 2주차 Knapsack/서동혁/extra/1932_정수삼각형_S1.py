n = int(input())
# n < 500 ==> 단순한 DP만 사용을 하게 되면 O(2 ^ N) 이고
# 2^10 ~= 1000 = 1k , 2^50 => 약 1,000,000,000,000,000임

Floor = []

for _ in range(n):
    Floor.append(list(map(int, input().split())))

def max_triangle(floor, index) -> int: # O(2^N) -> 시간초과
    if floor == n:
        return 0
    
    return Floor[floor][index] + max(max_triangle(floor + 1, index), 
                                     max_triangle(floor + 1, index + 1))

memoization = {}

def max_triangle2(floor, index) -> int: # O(N)
    key = (floor, index)
    
    if key not in memoization:
        if floor == n:
            memoization[key] = 0
        else:
            memoization[key] = Floor[floor][index] + max(max_triangle2(floor + 1, index), 
                                     max_triangle2(floor + 1, index + 1))
    # print(memoization)
    return memoization[key]

print(max_triangle2(0,0))