my_list=input().split()
my_new_list=[]
def agent_007(my_list):
	for item in my_list:
		if int(item)==0 or int(item)==7:
			my_new_list.append(int(item))
	for i in range(len(my_new_list)-2):
		if my_new_list[i]==0 and my_new_list[i+1]==0 and my_new_list[i+2]==7:
			return True
	return False
print(agent_007(my_list))