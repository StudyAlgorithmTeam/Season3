def hanoi_f(one, three, n):
    if n == 1:
        print(one,three)
        return

    hanoi_f(one, 6-one-three, n-1)
    print(one, three) 
    hanoi_f(6-one-three, three, n-1)

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi_f(1,3,n)
