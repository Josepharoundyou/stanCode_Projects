"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    To find the best match between the short dna sequence s2
    and the sub sequence of a long dna sequence s1.
    """
    s1 = input('Please give me a DNA sequence to search: ')        # long sequence to be looked up.
    s2 = input('What DNA sequence would you like to match? ')      # short sequence to be compared.
    check(s1, s2)


def check(a, b):
    """
    To compare.
    """
    count = len(a)-len(b)+1      # how many times are we going to match.
    best_match = ""
    match_num = 0
    for i in range(count):       # to extract the long dna sequence with the length of the short dna sequence.
        ch = a[i:i+len(b)]
        match = 0
        for j in range(len(b)):  # starting to compare.
            ch2 = ch[j]
            ch3 = b[j]
            if ch2.upper() == ch3.upper():
                match += 1
        if match_num < match:    # if this partial sequence of the long dna is better, keep it.
            match_num = match
            best_match = ch.upper()
    print(best_match)            # print the best matched part.






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
