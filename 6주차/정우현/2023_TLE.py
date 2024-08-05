import sys
input = sys.stdin.readline

N = int(input())

#소수 찾기 알고리즘
def prime_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True 

#10씩 곱해주면서 다음자리수의 소수를 찾는 알고리즘
def find_prime(n):
    #길이가 N과 같아지면 출력
    if len(str(n)) == N:
        print(n)
    else:
        #다음 자리에 숫자가 왔을 때 그 수가 소수인지 판단
        for i in range(1, 10):
            #다음 자리수를 구하는 방법
            num = n * 10 + i
            #짝수면 건너뛴다
            if i%2 == 0:
                continue
            #소수이면 다음자리수로 넘어간다
            if prime_num(num):
                find_prime(num)

#첫번째 숫자 하나부터 소수여서 2,3,5,7로 시작한다
find_prime(2)
find_prime(3)
find_prime(5)
find_prime(7)

#시간복잡도 :
#소수찾는데 걸리는 시간 : 2 ~ x번 반복
#N의 자리수라고 했을 때 모든 자리 수 마다 소수인지 판별해야 되는데 따라서 O(9^N)이다.