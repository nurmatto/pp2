your_nums=input().split()
def set_replacing(your_nums):
	my_new_list=list(dict.fromkeys(your_nums))
	print(my_new_list)
set_replacing(your_nums)