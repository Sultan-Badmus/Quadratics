import math
#Using the Almighty Formula
def Quadratic(a,b,c):
	d = (b**2) - 4*a*c
	if d == 0:
		print('You have repeated roots!')
	elif d > 0:
		print('You have simple roots!')
	else:
		print('You have complex roots!')
	
	print(f'The discriminant is {d}')

	if d>= 0:
		f = math.sqrt(d)/2*a
		x1, x2 = - (b/(2*a)) + f, - (b/(2*a)) - f
		x1 = round(x1, 2)
		x2 = round(x2, 2)

	else:
		d = (-d)
		f = math.sqrt(d)/2*a
		f = round(f,2)
		g = b/(2*a)
		g = round(g,2)
		x1 = str(g) + ' ' +  str('+') + ' ' + str(f) + 'i'
		x2 = str(g) + ' ' +  str('-') + ' ' + str(f) + 'i'
	

	print(f'Your roots are {x1} and {x2}.')
