"""
File: quadratic_solver.py
Name: Joseph
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program will solve the roots of equation: ax^2 + bx + c = 0
	"""
	print('stanCode Quadratic Solver! ')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	dis = b * b - 4 * a * c    # discriminant
	if dis > 0:
		y = math.sqrt(dis)
		x = (-b + y) / 2 * a
		print('Two roots: ' + str(x) + ',', end='')
		x = (-b - y) / 2 * a
		print(x)
		# When b^2-4ac > 0.
	elif dis < 0:
		print('No real roots')
		# To make sure b^2-4ac >0 otherwise can‘t do square root.
	else:
		y = math.sqrt(dis)
		x = (-b + y) / 2 * a
		print('One root: ' + str(x))
		# When b^2-4ac == 0.



















###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
