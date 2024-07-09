C, N = map(int, input().split())
# C : 적어도 C명 늘이기
# N : 도시의 개수

cost=[] # 홍보 시 드는 비용
customer=[] # 얻을 수 있는 고객의 수

for i in range(N):
    # a : 비용, b : 증원되는 사람 수
    a,b=map(int, input().split())
    cost.append(a)
    customer.append(b)

def f(c):
    if c<=0: return 0
    else:
        min_m = 999999999
        for i in range(0,N):
            min_m = min(min_m, f(c-cost[i])+customer[i])
        return min_m
    
print(f(C))
