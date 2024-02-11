my_list=input().split()
def returner(my_list):
	while len(my_list)!=0:
		print(my_list.pop(),end=' ')
returner(my_list)
		