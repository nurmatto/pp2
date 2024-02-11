from math import pi
radius=float(input())
def finder_volumer(radius):
	volume=(4/3)*pi*pow(radius, 3)
	return volume
print(finder_volumer(radius))
