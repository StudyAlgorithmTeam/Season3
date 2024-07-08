# 안녕 문제와 똑같은 방식
# 버틸 무게 (K)를 넘지 않는 선에서(cost[j-w[i]]) 한 배낭에 넣을 수 있는 물건들의 가치합 저장(cost)
# 최댓값(max(cost)) 출력

# ex) 입력
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# cost = [0, 0, 0, 6, 8, 12, 13, 14]


# 2
import sys
input=sys.stdin.readline
N, K=map(int, input().split()) # N : 물품 수, K : 버틸 무게

# l : [W,V]로 구성
l=[]
cost=[0]*(K+1)
for i in range(N):
    W, V = map(int, input().split()) # W : 물건 무게, V : 물건의 가치
    l.append([W,V])

for i in range(N):
    for j in range(K, l[i][0]-1,-1):
        cost[j]=max(cost[j], cost[j-l[i][0]]+l[i][1])
print(max(cost))



# 1 : 첫 풀이 (리스트 2개)
N, K=map(int, input().split()) # N : 물품 수, K : 버틸 무게

w=[]
v=[]

cost=[0]*(K+1)
for i in range(N):
    W, V = map(int, input().split()) # W : 물건 무게, V : 물건의 가치
    w.append(W)
    v.append(V)

for i in range(N):
    for j in range(K, w[i]-1,-1):
        # 
        cost[j]=max(cost[j], cost[j-w[i]]+v[i])
print(max(cost))
