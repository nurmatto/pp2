n = int(input('your number? '))
def checker_mecker(x):
	for i in range(0,x+1):
		if i%12==0:
			yield i
x = list(checker_mecker(n))
for i in x:
	print(i,end=' ')