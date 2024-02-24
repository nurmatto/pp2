n = int(input())
def even_checker(x):
	for i in range(0,x+1):
		if i%2==0:
			yield i
nurma_list = list(even_checker(n))
new_one=''
for i in nurma_list:
	i=str(i)
	new_one = new_one + i + ','
print(new_one[0:len(new_one)-1])