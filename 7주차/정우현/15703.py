N = int(input())
arr = list(map(int, input().split()))

# 주사위를 오름차순으로 정렬합니다.
arr.sort()

dice_arr = [0] * N
#주사위의 개수를 추척하는 배열

count = 0
#주사위 탑의 수

for i in arr:
    top = False
    #어느 탑인지 구분하기 위해 사용
    for j in range(count):
        if dice_arr[j] <= i:
            dice_arr[j] += 1
            top = True
            break
            #어느 탑에 올릴지 찾으면 거기서 멈춤
    
    #for 문에서 통과되지 못하면 새로 탑을 만든다.
    if not top:
        dice_arr[count] = 1
        count += 1

print(count)