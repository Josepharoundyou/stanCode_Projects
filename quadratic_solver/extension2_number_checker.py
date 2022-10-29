"""
File: extension2_number_checker.py
Name: Joseph
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100

def main():
    """
    This program determines if the input is a
    perfect number、deficient number or an abundant number.
    """
    while True:
        n = int(input('n = '))
        # input a integer which is >1.
        if n == EXIT:
            print('Have a good one!')
            break
            # End this program if you input the exact number.
        a = n
        summary = 0
        while True:
            a -= 1
            if a > 0:
                count = divide(a, n)
                summary = total(count, summary)
            else:
                if summary == n:
                    print(str(n) + ' is a perfect number')
                elif summary > n:
                    print(str(n) + ' is an abundant number')
                else:
                    print(str(n) + ' is a deficient number')
                break


def divide(a, n):
    """
    To find out all the factor of the input number.
    :param a: int, the denominator.
    :param n: int, the numerator.
    """
    if n % a == 0:
        return a
    return 0


def total(count, summary):
    """
    :param count: int, the number to be added.
    :param summary: int, the total amount.
    """
    summary += count
    return summary


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
