"""
File: extension1_factorial.py
Name: Joseph
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program will calculate the factorial result of
	the user input number.
	"""
	print('Welcome to stanCode factorial master! ')
	while True:
		data1 = int(input('Give me a number, and I will list the answer of factorial: '))
		if data1 == EXIT:
			print('------See ya!------')
			break
		else:
			factorial(data1)


def factorial(data1):
	"""
	To count the factorial result of the user input.
	:param:int, >0.
	:return: str, Answer.
	"""
	data2 = data1
	for i in range(data1):
		if data1 > 1:
			data1 -= 1
			data2 *= data1
	return print('Answer: '+str(data2))


if __name__ == '__main__':
	main()