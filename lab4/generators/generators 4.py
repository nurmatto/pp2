a = int(input())
b = int(input())

def yielder_squarer(x,y):
	for number in range(x, y+1):
		yield number

nurma = yielder_squarer(a,b)

for i in nurma:
	print(i, end=' ')