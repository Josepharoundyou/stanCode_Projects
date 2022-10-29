"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, number to be check.
	:return: integer
	"""
	rest = 0
	if n < 0:
		n *= -1
	num = helper(n, rest)
	return num


def helper(n, rest):
	"""
	:param n: int, the rest of the number to be checked.
	:param rest: int, the digit to be compared.
	:return: int, the largest digit.
	"""
	rest1 = n % 10
	if rest1 == 0 and n == 0:
		return rest
	if rest1 > rest:
		rest = rest1
	return helper(n//10, rest)

if __name__ == '__main__':
	main()
