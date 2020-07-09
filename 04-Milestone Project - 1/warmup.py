#!/usr/bin/env python3

def display_game(game_list):
    print('\nHere is the current list')
    print(game_list)

def user_choice():

    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    within_range = False

    # While the choice is not a digit, keep asking for input
    while choice.isdigit() == False or within_range == False:

        # We shouldn't convert here, otherwise we get an error on a wrong input
        choice = input('Please enter a number (0-10): ')

        # Error message check
        # If digit provided
        if choice.isdigit() == False:
            print('Sorry that is not a digit!')
        # If within range
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                print('Sorry, but digit is out of range!')
                within_range = False

    # We can convert once the while loop above has confirmed we have a digit
    return int(choice)

def position_choice():

    # This original choice value can be anything that isn't an integer
    choice = 'wrong'

    # While the choice is not in list, keep asking for input.
    while choice not in ['0', '1', '2']:

        # We shouldn't convert here, otherwise we get an error on a wrong input
        choice = input('Pick a position to replace (0, 1, 2): ')

        if choice not in ['0', '1', '2']:
            # This clears the current output below the cell
            print('Sorry, but you did not choose a valid position (0, 1, 2)')

    return int(choice)

def replacement_choice(game_list, position):

    user_placement = input('Type a string to place at the position: ')

    game_list[position] = user_placement

    return game_list

def gameon_choice():

    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'

    # While the choice is not in list, keep asking for input.
    while choice not in ['Y', 'N']:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input('Whould you like to keep playing? Y/N: ')

        if choice not in ['Y', 'N']:
            # This clears the current output below the cell
            print("Sorry, I didn't understand. Please make sure you choose Y or N")

    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False

if __name__ == "__main__":
    # Variable to keep game playing
    game_on = True

    # First game list
    game_list = [0, 1, 2]

    while game_on:

        # Clear any historical output and show the game list
        display_game(game_list)

        # Have player choose position
        position = position_choice()

        # Rewrite that position and update game_;ist
        game_list = replacement_choice(game_list,position)

        # Clear Screen and show the updated game list
        display_game(game_list)

        # Ask if you want to keep playing
        game_on = gameon_choice()