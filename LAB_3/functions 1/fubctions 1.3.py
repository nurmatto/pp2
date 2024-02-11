nlegs,nheads=94,35
def solve(nheads,nlegs):
	'''
by elimination i got 
4R+2ch=94
R+ch=35
ch=23, x=12
    '''
	rabbits=(nlegs-2*nheads)/2
	chickens=nheads-rabbits
	return chickens, rabbits
print(solve(nheads, nlegs))