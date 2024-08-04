import sys
input=sys.stdin.readline

# O(1)
K, N=map(int,input().split())

# O(K)
l=[int(input()) for _ in range(K)]

# O(1)
start=1

#O(K) (l : K개의 원소)
end=max(l)

# O(log(n)) -> n : max(l)
# 이진 탐색 : start가 end보다 작거나 같을 때까지 반복
# -> 매 루프마다 탐색 범위 절반으로 줄어듬 --> O(log(n))
while start<=end:
    cnt=0
    mid=(start+end)//2
    # O(K)
    # 리스트(l)의 각 랜선을 mid값으로 나누어 더함
    for i in l:
        cnt+=i//mid
    if cnt<N:
        end=mid-1
    else:   # cnt >= N
        start=mid+1
print(end)

# 이진 탐색 루프 : O(log N), 랜선 자르기 작업 : O(K)
# ∴ 전체 시간복잡도 : O(K log(N))
