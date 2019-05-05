#!/usr/bin/env python3
import os
import random

def display_board(board):
	os.system('clear')
	#print('   |   |   ')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
	#print('   |   |   ')
	print('--- --- ---')
	#print('   |   |   ')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
	#print('   |   |   ')
	print('--- --- ---')
	#print('   |   |   ')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
	#print('   |   |   ')
	pass

def player_input():
	marker = ''
	#while marker != 'X' and marker != 'O'
	while not (marker == 'X' or marker == 'O'):
		marker = input("Please pick a marker 'X' or 'O': ").upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, mark):
	return (
	(board[7] == board[8] == board[9] == mark) or # Top horizontal
	(board[4] == board[5] == board[6] == mark) or # Middle horizontal
	(board[1] == board[2] == board[3] == mark) or # Bottom horizontal
	(board[1] == board[4] == board[7] == mark) or # Left vertical
	(board[2] == board[5] == board[8] == mark) or # Middle vertical
	(board[3] == board[6] == board[9] == mark) or # Right vertical
	(board[3] == board[5] == board[7] == mark) or # Diagonal bot-rigth - top-left
	(board[1] == board[5] == board[9] == mark)) # Diagonal bot-left - top-rigth

def choose_first():
	if random.randint(0,1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
	#return not ' ' in board
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True

def player_choice(board):
	position = 0
	while position not in range(1,10) or not space_check(board, position):
		position = int(input('Please enter a number [1-9]: '))
	return position

def replay():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



print('Welcome to Tic Tac Toe!')

while True:
	#board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	board = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first!')

	play_game = input('Do you want to play? [Y]es [N]o? ')

	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':
			display_board(board)
			print('{} turn'.format(turn))
			position = player_choice(board)
			place_marker(board, player1_marker, position)
			
			if win_check(board, player1_marker):
				display_board(board)
				print('Congratulations! Player 1 won the game!')
				game_on = False
			else:
				if full_board_check(board):
					print('Draw!')
					break
				else:
					turn = 'Player 2'
		else:
			display_board(board)
			print('{} turn'.format(turn))
			position = player_choice(board)
			place_marker(board, player2_marker, position)
			
			if win_check(board, player2_marker):
				display_board(board)
				print('Congratulations! Player 2 won the game!')
				game_on = False
			else:
				if full_board_check(board):
					print('Draw!')
					break
				else:
					turn = 'Player 1'

	if not replay():
		break