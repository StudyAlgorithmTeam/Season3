N = int(input()) #사람의 수

L = list(map(int,input().split())) #각 사람마다 잃는 체력
J = list(map(int,input().split())) #각 사람마다 얻는 기쁨

def maxjoy(i,life):
    if life <= 0: #life 값이 0보다 작아지면 이 값이 선택 되지 않게 -100을 준다
        return -100
    if i == N: #끝까지 다 보면 종료
        return 0
    
    return max((J[i] + maxjoy(i+1, life - L[i]))#인사를 하는 경우
               , maxjoy(i+1,life)#인사를 하지 않는 경우
               )

print(maxjoy(0,100))



#dp
#100이 넘어가면 다음부터 100이 될때까지 더해서 비교?
#dp --> 점화식 : 멱등성이 지켜지는 함수를 만들어라
#선택할지 말지를 정해서 트리처럼 퍼져나간다
# i ~ N 까지 인사를 했을 때 max_joy를 찾아야 됨
#인사를 하면 j[i] +maxjoy(i+1,L-L[i])
#안하면 max_joy(i+1,L)
#둘중 최대값
#인사를 했는데 죽으면 절대 선택되지 않을 값을 줘야됨
#이다음에는 hash를 이용해서 풀어봐라
