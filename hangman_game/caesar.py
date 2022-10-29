"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    To solve the encrypted string.
    """
    number = int(input('Secret number: '))
    cipher = input("What's the ciphered string?")
    new_alphabet = ALPHABET[26-number:]+ALPHABET[:26-number]
    ans = ""
    for i in range(len(cipher)):
        ch = cipher[i].upper()
        if ch.isalpha():
            ans += ALPHABET[new_alphabet.find(ch):new_alphabet.find(ch) + 1]
        else:
            ans += ch
    print('The deciphered string is: ' + str(ans))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
