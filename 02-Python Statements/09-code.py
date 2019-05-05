#!/usr/bin/env python3

import random

num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:
	try:
		guess = int(input("\nI'm thinking of a number between 1 and 100.\n  What is your guess? "))
	except Exception as e:
		print('Choose a number! Please try again!')
		continue

	if guess < 1 or guess > 100:
		print('Out of bonds! Please try again!')
		continue

	if guess == num:
		print("\nCongratulations! You guessed it! It takes you {} guesses!".format(len(guesses)))
		break

	guesses.append(guess)

	if guesses[-2]:
		if abs(num - guess) < abs(num - guesses[-2]):
			print('WARMER!')
		else:
			print('COLDER!')
	else:
		if abs(num - guess) <= 10:
			print('WARM!')
		else:
			print('COLD!')