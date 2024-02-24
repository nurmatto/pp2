from math import tan,pi

n = int(input('Input number of sides: '))
length = int(input('Input the length of a side: '))

print('The area of the polygon is:', (1/4)*n*(length**2)*tan(pi/n)**-1)