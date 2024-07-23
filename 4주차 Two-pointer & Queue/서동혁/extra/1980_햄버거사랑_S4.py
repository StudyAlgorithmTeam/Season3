n, m, t = map(int,input().split())

small = min(n,m)
big = max(n,m)

small_burger = t // small
big_burger = 0
coke = t - (small_burger * small + big_burger * big)
temp = []

while(small_burger >= 0):
    temp.append((coke, small_burger+big_burger))
    if coke == 0:
        break
    
    big_burger += 1    
    while(small_burger * small + big_burger * big > t):
        small_burger -= 1
    
    coke = t - (small_burger * small + big_burger * big)

a = sorted(temp, key=lambda x: (x[0],-x[1]))
print(a[0][1],a[0][0])