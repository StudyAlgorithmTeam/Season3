n = int(input())
lost = list(map(int, input().split()))
get = list(map(int, input().split()))

def DP(index, life): # memoization을 사용하지 않고 DP만 사용했을 때
    if life <= 0:
        return -101
        # max 값이 100이고 get[index] + DP(index+1,health)
        # 이므로 get[index] 값보다 빼주는 DP 값이 커야 조건 만족시킴
    
    if index == n:
        return 0

    return max(DP(index+1,life), get[index]+DP(index+1, life-lost[index]))

print(DP(0,100))

cache = {} # dictionary를 사용해 memoization => 400ms에서 40ms로 줄어듬

def max_joy(index, life) -> int:
    key = (index, life)
    if key not in cache:
        if life <= 0:
            cache[key] = -101
        elif index == n:
            cache[key] = 0
        else:
            cache[key] = max(max_joy(index+1,life), get[index]+max_joy(index+1,life-lost[index]))

    return cache[key]

print(max_joy(0,100))