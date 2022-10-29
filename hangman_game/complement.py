"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    To find the complement strand of a DNA sequence.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    build_complement(dna)


def build_complement(a):
    """
    This function finds the complement strand of the input dna.
    :param a:str, dna sequence.
    """
    ans = ""
    for i in range(len(a)):
        ch = a[i]
        if ch.upper() == "A":
            ans += "T"
        elif ch.upper() == "T":
            ans += "A"
        elif ch.upper() == "G":
            ans += "C"
        elif ch.upper() == "C":
            ans += "G"
    return print("The complement of " + str(a) + " is " + str(ans))


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
