T = int(input())

for _ in range(T):
	N = int(input())
	price = 0

	for i in range(N):
		temp = list(map(str,input().split()))
		count = int(temp[1])
		price = price + count*float(temp[2])
	print("$",end='')
	print("{:.2f}".format(price))
	