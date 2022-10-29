"""
File: boggle.py
Name: Joseph Huang
----------------------------------------
To search through words that's been combined with those input letters.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	To check if a word exists by searching through it.
	"""
	start = time.time()
	####################
	lst_ind = combine()
	dic_lst = read_dictionary()
	find_anagram(lst_ind, dic_lst)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def combine():
	"""
	To combine all inputs.
	:return: lst, nested list combined with inputs.
	"""
	while True:
		lst_ind = []
		first = input('1 row of letters')
		if check_input(first):
			second = input('2 row of letters')
			if check_input(second):
				third = input('3 row of letters')
				if check_input(third):
					forth = input('4 row of letters')
					if check_input(forth):
						lst_ind += [change(first)]
						lst_ind += [change(second)]
						lst_ind += [change(third)]
						lst_ind += [change(forth)]
						break
	return lst_ind


def change(b):
	"""
	To be case-insensitive.
	:param b: str, inputs.
	:return: lst, combined by inputs.
	"""
	b_split = b.split()
	new_lst = []
	for ch in b_split:
		ch_case_insensitive = str(ch).lower()
		new_lst += [ch_case_insensitive]
	return new_lst


def check_input(a):
	"""
	To check if the form of the input is suitable.
	:param a: str, input string.
	:return: bool, if the form is suitable.
	"""
	for ch in a.split():
		if len(ch) != 1 or ch.isalpha() is not True:
			print('Illegal input')
			return False
	return True


def find_anagram(lst, dic_lst):
	"""
	To check if a word exists by searching through it.
	:param lst: list, input letters.
	:param dic_lst: list, dictionary.
	"""
	all_words = []
	for x in range(4):
		for y in range(4):
			sub_s = ""
			index_place = []
			sub_s += lst[x][y]
			index_place.append([x, y])
			helper_find_anagram(lst, dic_lst, x, y, sub_s, all_words, index_place)
	# print(all_words)
	print(f"There are {len(all_words)} in total")


def helper_find_anagram(lst, dic_lst, x, y, sub_s, all_words, index_place):
	"""
	Helper function
	:param lst: list, input letters.
	:param dic_lst: list, dictionary.
	:param x: int, index of the list.
	:param y: int, index of the word in the x's list.
	:param sub_s: str, words to be found.
	:param all_words: list, all words that has been recorded.
	:param index_place: list, index of all the letters that's been searched right away.
	"""
	if len(sub_s) >= 16:
		pass
	else:
		for a in range(x - 1, x + 2):
			if 0 <= a < 4:
				for b in range(y-1, y+2):
					if 0 <= b < 4:
						if [a, b] not in index_place:
							# Choose
							sub_s += lst[a][b]
							x, y = a, b
							index_place.append([a, b])
							# Explore
							if has_prefix(sub_s, dic_lst):
								if len(sub_s) >= 4 and find_word(sub_s, dic_lst) and sub_s not in all_words:
									print(f'Found :"{sub_s}"')
									all_words.append(sub_s)
								helper_find_anagram(lst, dic_lst, x, y, sub_s, all_words, index_place)
							# Un-choose
							sub_s = sub_s[:-1]
							index_place.pop()
							x, y = index_place[-1][0],index_place[-1][1]


def find_word(sub_s, dic_lst):
	"""
	To find word in the dictionary.
	:param sub_s: str, word to be found.
	:param dic_lst: list, dictionary.
	:return: bool.
	"""
	for word in dic_lst:
		if word == sub_s:
			return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			dic_lst.append(line.strip())
	return dic_lst


def has_prefix(sub_s, dic_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic_lst:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
