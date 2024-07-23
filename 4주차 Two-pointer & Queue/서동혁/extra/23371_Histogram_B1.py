n,s,k = map(int,input().split())
k_list = list(map(int,input().split()))

number = [0] * n

for item in k_list:
    if item % s == 0:
        number[item//s - 1] += 1
    else:
        number[item//s] += 1

maximum = max(number)

while(maximum != 0):
    for i in range(n):
        if number[i] < maximum:
            print(".", end='')
        else:
            print("#", end='')
            number[i] -= 1
    maximum -= 1
    print()
print("-" * n)
    



1-10 // 11-20 // 21-30