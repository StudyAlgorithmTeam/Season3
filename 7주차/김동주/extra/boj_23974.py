# 짝수 게임

N, K = map(int, input().split())


if N % 2 == 0:
    print('YG' if ((K % 6) != 1) else 'HS')
else:
    print('YG' if ((K % 6) not in (0, 5,)) else 'HS')
