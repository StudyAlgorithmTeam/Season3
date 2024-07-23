N = int(input()) # 50

for i in range(1,N+1):
    C = int(input()) # 1000
    I = int(input()) # 2000
    P = list(map(int,input().split()))

    item1 = 0
    item2 = 0

    for index1 in range(I):
        check = False
        temp = P[index1]
        for index2 in range(index1+1,I):
            if temp + P[index2] == C:
                check = True
                item1 = index1 + 1
                item2 = index2 + 1
                break
        if check:
            break
    print(f"Case #{i}: {item1} {item2}")