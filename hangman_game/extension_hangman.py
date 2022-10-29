"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    """
    ans = random_word()  # this program will randomly pick a word as an answer.
    guess = ""
    for i in range(len(ans)):
        guess += "_"  # To show the dashed word.
    print('The word looks like ' + str(guess))
    print('You have ' + str(N_TURNS) + ' wrong guesses left. ')
    a = N_TURNS
    guess_it(ans, guess, a)


def guess_it(ans, guess, a):
    """
    Start to guess!
    """
    while True:
        answer_ch = input('Your guess: ')
        if answer_ch.isalpha():
            guess_new = ""
            right = 0
            for j in range(len(ans)):                # To check new guess.
                ch = ans[j]
                if answer_ch.upper() == ch:
                    guess_new += str(ch)
                    right += 1
                else:
                    if guess[j].isalpha():
                        guess_new += guess[j]
                    else:
                        guess_new += "_"
            guess = guess_new
            if guess == ans:                                            # You got the right answer.
                print('You are correct! ')
                print('You win!!')
                print('The word was: ' + str(guess_new))
                break
            else:
                if right > 0:                                          # If you are correct, but u still got missing words.
                    print('You are correct! ')
                    print('The word looks like ' + str(guess))
                    print('You have ' + str(a) + ' wrong guesses left. ')
                    right = 0
                    hang_pic(a)
                else:                                                                   # If you are wrong.
                    a -= 1
                    if a > 0:                                                           # but with more than one guess left.
                        print('There is no ' + str(answer_ch) + "\'s in the word.")
                        print('The word looks like ' + str(guess))
                        print('You have ' + str(a) + ' wrong guesses left. ')
                        hang_pic(a)
                    else:                                                               # You are completely hung.
                        print('You are completely hung :( ')
                        print('The word was ' + str(ans))
                        hang_pic(a)
                        break
        else:
            print('Illegal format. ')


def hang_pic(a):
    """
    To present hang picture.
    """
    print('_______')
    if a == 7:
        for i in range(a - 2):
            print('|')
    elif a == 6:
        print('|   |')
        for i in range(a-2):
            print('|')
    elif a == 5:
        print('|   |')
        print('|  ( )')
        for i in range(a - 2):
            print('|')
    elif a == 4:
        print('|   |')
        print('|  ( )')
        print('|   |')
        for i in range(a - 2):
            print('|')
    elif a == 3:
        print('|   |')
        print('|  ( )')
        print('|  /|')
        for i in range(a - 1):
            print('|')
    elif a == 2:
        print('|   |')
        print('|  ( )')
        print('|   |')
        print('|  /|\\')
        for i in range(a):
            print('|')
    elif a == 1:
        print('|   |')
        print('|  ( )')
        print('|   |')
        print('|  /|\\')
        print('|  /')
        for i in range(a):
            print('|')
    else:
        print('|   |')
        print('|  (X)')
        print('|   |')
        print('|  /|\\')
        print('|  / \\')
    print('-------')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()


