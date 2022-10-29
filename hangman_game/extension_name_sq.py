"""
File: name_sq.py (extension)
Name: 
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    print the square pattern of the input name.
    """
    print('This program prints a name in a square pattern! ')
    name = input('Name: ')
    square(name)


def square(a):
    """
    print the square pattern of the name.
    :param a:str, given name.
    """
    print(a)                               # first line.
    for i in range(len(a)-2):
        ch = a[i+1]
        print(ch, end="")                  # middle part.
        for j in range(len(a)-2):
            print(" ", end="")
        ch2 = a[len(a)-2-i:len(a)-1-i]
        print(ch2)
    ans = ""
    for k in range(len(a)):
        ch3 = a[k]
        ans = ch3 + ans
    print(ans)                            # The reversed given name.



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
