my_list=input().split()
def checker_33(my_list):
	for i in range(len(my_list)-1):
		if int(my_list[i])==3 and int(my_list[i+1])==3:
			return True
	return False
print(checker_33(my_list))