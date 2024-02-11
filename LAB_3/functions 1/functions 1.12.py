my_list=input().split()
def checker_mecker(my_list):
	for number in my_list:
		for i in range(int(number)):
			print('*',end='')
		print()
checker_mecker(my_list)
