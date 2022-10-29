"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    To find all the anagram(s)
    for the word input by user.
    """

    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        start = time.time()
        ##########################
        word_to_test = input('Find anagram for: ')
        if word_to_test == EXIT:
            break
        find_anagrams(word_to_test)
        ##########################
        end = time.time()
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    print('----------------------------------')


def read_dictionary():
    """
    :return: dictionary.
    to read the dictionary.
    """
    with open(FILE, 'r') as f:
        lst = []
        for line in f:
            lst.append(line.strip())
        return lst


def find_anagrams(s):
    """
    :param s: str, user input.
    fina all diagrams.
    """
    print('Searching...')
    sub_s = ''
    all_diagram = []
    find_anagram_helper(s, sub_s, all_diagram)
    print(all_diagram)


def find_anagram_helper(s, sub_s, all_diagram):
    if len(sub_s) == len(s):
        diagram = search_dic(sub_s)
        if diagram is not None:
            # First diagram.
            if len(all_diagram) == 0:
                all_diagram.append(diagram)
                print('Found:' + sub_s)
                print('Searching...')
            # More than one diagram.
            elif sub_s in all_diagram:
                pass
            else:
                all_diagram.append(diagram)
                print('Found:' + sub_s)
                print('Searching...')
    else:
        for ch in s:
            # Choose
            sub_s += ch
            # Explore
            # or has_prefix(sub_s) is False
            if s.count(ch) >= sub_s.count(ch) and has_prefix(sub_s):
                find_anagram_helper(s, sub_s, all_diagram)
            else:
                pass
            # Un choose
            sub_s = sub_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, substring of the user input
    :return: bool, if the sub_s is in the dictionary.
    """
    lst = read_dictionary()
    for word in lst:
        if word.startswith(sub_s):
            return True


def search_dic(sub_s):
    lst = read_dictionary()
    for word in lst:
        if sub_s == word:
            return sub_s


if __name__ == '__main__':
    main()
