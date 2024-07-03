A = int(input())
X = int(input())

MOD_NUM = 1000000007
# print(pow(A,X,MOD_NUM))

my_list = [(1,A)]
count = 1

while(True):
    count = count * 2

    if count > X:
        break
    
    tmp_num = (my_list[-1][1] * my_list[-1][1]) % MOD_NUM
    my_list.append((count,tmp_num))

result = 1

for i in my_list[::-1]:
    if X >= i[0]:
        X = X - i[0]
        result = result * i[1] % MOD_NUM
    if X == 0:
        break

print(result)