"""
File: prime_checker.py
Name: Joseph
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program will decide whether the input number is a prime number or not.
	"""
	print('Welcome to the prime checker! ')
	while True:
		n = int(input('n = '))
		# input a integer which is >1.
		if n == EXIT:
			print('Have a good one !')
			break
			# End this program if you input the exact number.
		a = n
		prime_check(a, n)


def prime_check(a, n):
	"""
	To check if the input number is a prime or not.
	:param a:int, input number.
	:param n:int, input number.
	:return1:str, not a prime number.
	:return2:str, a prime number.
	"""
	while True:
		a -= 1
		if a > 1:
			if n % a == 0:
				# If it's not a prime number, then it can be divided by an integer that is greater than 1 and smaller than itself.
				return print(str(n) + ' is not a prime number.')

		else:
			return print(str(n) + ' is a prime number.')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
