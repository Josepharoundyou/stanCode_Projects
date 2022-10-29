"""
File: hailstone.py
Name: Joseph
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program will simulate the execution of the Hailstone sequence.
    """
    print('This program computes Hailstone sequences. ')
    print('')
    n = int(input('Enter a number: '))
    b = n
    c = 0
    if n <= 0:
        pass
        # If you entered a number <= 0
    elif n == 1:
        print('It took ' + str(c) + ' steps to reach 1.')
        # If you input 1.
    else:
        c = 1
        while True:
            a = hailstone(b)
            # Stimulate hailstone.
            if a == 1:
                print(str(b) + ' is even, so I take half: ' + str(a))
                print('It took ' + str(c) + ' steps to reach 1.')
                # Last step before you get 1.
                break
            elif a % 2 != 0:
                if b % 2 == 0:
                    print(str(b) + ' is even, so I take half: ' + str(a))
                    # when b is even.
                else:
                    print(str(b) + ' is odd, so I make 3n+1: ' + str(a))
                    # when b is odd.
                b = a
                # reassign b
                c += 1
                # count
            else:
                if b % 2 == 0:
                    print(str(b) + ' is even, so I take half: ' + str(a))
                    # when b is even.
                else:
                    print(str(b) + ' is odd, so I make 3n+1: ' + str(a))
                    # when b is odd.
                b = a
                # reassign b
                c += 1
                # count


def hailstone(b):
    """
    simulates the execution of the Hailstone sequence,
    defined by Douglas Hofstadter.
    :param b: int, input number.
    :return1: int, divided by 2.
    :return2: int, b*3+1.
    """
    if b % 2 == 0:
        b //= 2
        # when b is even.
        return b
    b = b*3+1
    # when b is odd.
    return b


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
