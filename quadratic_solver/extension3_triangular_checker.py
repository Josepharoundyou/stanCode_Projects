"""
File: extension3_triangular_checker.py
Name: Joseph
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program will decide whether the user input
    is an triangular number or not.
    """
    print('Welcome to the triangular number checker! ')
    while True:
        data1 = int(input('n: '))
        if data1 == EXIT:
            print('Have a good one!')
            break
        else:
            triangular_check(data1)


def triangular_check(data1):
    """
    to check if the input is a triangular or not.
    :param:int, number to be checked.
    :return1:str, it's a triangular.
    :return2:str, it's not a triangular
    """
    data2 = data1
    while data1 > 0:
        n = data1
        if n*(n + 1)/2 == data2:
            return print(str(data2) + ' is a triangular number')
        data1 -= 1
    return print(str(data2) + ' is not a triangular number')


if __name__ == '__main__':
    main()


# MY OLD ANSWER!!!!!!!!!!!!!!!!
# please ignore this!!!!!!!
# EXIT = -100
#
#
# def main():
#     """
#     This program will decide whether the user input
#     is an triangular number or not.
#     """
#     print('Welcome to the triangular checker! ')
#     while True:
#         data1 = int(input('n: '))
#         if data1 == EXIT:
#             break
#         else:
#             n = triangular_check(data1)
#             if n > 0:
#                 print(str(data1) + ' is a triangular number')
#             else:
#                 print(str(data1) + ' is not a triangular number')
#
#
# def triangular_check(data1):
#     """
#     param
#     """
#     data2 = data1
#     while data1 > 0:
#         data1 -= 1
#         n = data1
#         if n*(n + 1)/2 == data2:
#             return n
#         else:
#             pass
#     n = 0
#     return n
