N = int(input())

tile = [0] * (N+1)

if N % 2 == 1:
    print(0)
else:
    tile[2] = 3
    for i in range(4, N+1, 2):
        tile[i] = 3*tile[i-2] + 2*sum(tile[0:i-2:2]) + 2
    
    print(tile[N])

# 2 이상의 tile들은 그림 힌트에서 4개의 타일을 한번에 만드는 방법이 2개인 것 처럼
# 6개도 2개, 8개도 2개 ..... 있으므로 +2를 해줘야한다.
# ex) 6개 타일
#  ㅡㅡㅡㅡㅡㅡ     ㅣ ㅡㅡㅡㅡ ㅣ
# ㅣ ㅡㅡㅡㅡ ㅣ    ㅣ ㅡㅡㅡㅡ ㅣ
# ㅣ ㅡㅡㅡㅡ ㅣ     ㅡㅡㅡㅡㅡㅡ