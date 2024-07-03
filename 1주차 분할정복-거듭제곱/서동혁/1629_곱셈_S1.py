def solution(a, b, c):
    if b == 1:
        return a % c

    temp = solution(a, b // 2, c)

    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    else:
        return (temp * temp) % c

A, B, C = map(int, input().split())

print(solution(A, B, C))

# print(pow(A,B,C)) -> 이렇게는 한줄 출력 가능
# pow 함수는 base, exp, mod=None 매개변수를 받음
# mod는 없어도 됨.
