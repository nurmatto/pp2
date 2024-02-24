# each step and i more near to my goal
n = int(input('Your number?) '))

def party_maker(x):
	while x!=-1:
		yield x
		x-=1
nurma = party_maker(n)
for i in nurma:
	print(i,end=' ')