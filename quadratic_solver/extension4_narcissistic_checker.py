"""
File: extension4_narcissistic_checker.py
Name: Joseph
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program checks if the user input is a narcissistic number or not.
    """
    print('Welcome to the narcissistic number checker!')
    while True:
        data1 = int(input('n: '))
        if data1 == EXIT:
            print('Have a good one! ')
        else:
            narcissistic(data1)


def narcissistic(a):
    """
    To decide
    """
    data1 = a  # To keep the original input number
    first = find1(a)  # To find the first digit of the input number
    times = find2(a)  # To figure out how many times can the input number be divided by 10 to reach the first digit.
    t = times  # To keep the original times.
    data2 = 0
    # Start counting!!!!!
    for i in range(times+1):
        data2 += first**(t+1)  # variable_first to the power of t.
        a = a - first*(10**times)  # To erase the first digit.
        times -= 1
        first = a//10**times  # To find the next digit.
    if data2 == data1:
        print(str(data1) + ' is a narcissistic number')
    else:
        print(str(data1) + ' is not a narcissistic number')


def find1(b):
    """
    To find the first digit.
    :param: int, input number.
    :return: int, first digit.
    """
    times = 0
    while True:
        first = b//10**times
        if first > 9:
            times += 1
        else:
            return first


def find2(c):
    """
    To figure out how many times can the input number be divided by 10 to reach the first digit.
    :param: int, input number.
    :return: int, how many times.
    """
    times = 0
    while True:
        first = c//10**times
        if first > 10:
            times += 1
        else:
            return times


if __name__ == '__main__':
    main()
