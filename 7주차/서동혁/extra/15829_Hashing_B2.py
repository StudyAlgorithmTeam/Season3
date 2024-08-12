L = int(input())
s = input()

r = 31
M = 1234567891
result = 0

for i in range(L): # O(L)
    result = (result + (ord(s[i])-96) * r**i) % M
print(result)