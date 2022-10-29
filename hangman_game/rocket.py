"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 4


def main():
    """
    This program prints a rocket with the size
    that will be determined by the constant(SIZE)
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    The head of the rocket.
    """
    for i in range(SIZE):
        for j in range(SIZE, i, -1):  # Print left side of the head.
            print(" ", end="")
        for k in range(i + 1):
            print("/", end="")
        for l in range(i + 1):        # Print right side of the head.
            print('\\', end="")
        print("")


def belt():
    """
    The belt of the rocket.
    """
    print("+", end="")
    for i in range(SIZE*2):
        print("=", end="")
    print("+")


def upper():
    """
    The up-middle side of the rocket.
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(SIZE - 1, i, -1):
            print('.', end="")
        for k in range(i + 1):
            print('/\\', end="")
        for l in range(SIZE - 1, i, -1):
            print('.', end="")
        print("|")


def lower():
    """
    The lower-middle side of the rocket.
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print('.', end="")
        for k in range(SIZE, i, -1):
            print('\\/', end="")
        for l in range(i):
            print('.', end="")
        print("|")


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
    main()
