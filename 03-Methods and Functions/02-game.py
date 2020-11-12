#!/usr/bin/env python3
from random import shuffle

def shuffle_list(mylist):
    # Take in list and return it after shuffle
    shuffle(mylist)

    return mylist

def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        # Recall input() returns a string
        guess = input('Pick a number - 0, 1, 2: ')

    return int(guess)

def check_guess(mylist, guess):

    if mylist[guess] == '0':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time!')
        print(mylist)
    
if __name__ == "__main__":
    # Initial list
    my_list = [' ', '0', ' ']

    # Shuffle list
    game_list = shuffle_list(my_list)

    # Get user's guess
    guess = player_guess()

    # Check user's guess
    check_guess(game_list, guess)
