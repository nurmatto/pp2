my_list=input().split()

def filter_prime(my_list):
	prime_list=[]
	for number in my_list:
		is_prime=True
		for i in range(2,int(number)):
			if int(number)%i==0:
				is_prime=False
				break
		if is_prime and int(number)>1:
			prime_list.append(int(number))
	print(prime_list)
	
filter_prime(my_list)