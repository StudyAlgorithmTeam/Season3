# 싫은데요

N, M = map(int, input().split())
A = [*map(int, input().split())]


covered_volume = 0
max_covered_volume = 0


s = 0 # 막기 시작한 구멍의 위치
e = 0 # 다음에 막아볼 구멍의 위치

# 시작 지점을 정한다.
# 구멍의 크기가 몸보다 큰 경우가 있을지도 모른다.
# 너무 큰 구멍은 적당히 건너뛰자.
while s < N and M < A[s]:
    s += 1
    e += 1

# 연속한 구멍을 막아햐 하므로, 투 포인터를 이용한 큐 방식으로 문제에 접근한다.
while e < N:
    # e번 구멍을 막을 수 없다면 앞 부분 구멍을 포기하여 최대한 부피를 확보한다.
    while s <= e and M-covered_volume < A[e]:
        covered_volume -= A[s]
        s += 1

    if M-covered_volume < A[e]:
        # 그래도 e번 구멍을 막을 수 없을 수도 있다.
        covered_volume -= A[s]
        s += 1
        e += 1
    else:
        # 성공적으로 막았다면 이 때 막은 부피를 기억하자.
        covered_volume += A[e]
        if max_covered_volume < covered_volume:
            max_covered_volume = covered_volume
        e += 1

print(max_covered_volume)
