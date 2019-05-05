#!/usr/bin/env python3

print('\n## Problem 1')
try:
	for i in ['a','b','c']:
		print(i**2)
except TypeError:
	print('There is an TypeError expetion!')

print('\n## Problem 2')
x = 5
y = 0
try:
	z = x/y
except ZeroDivisionError:
	print("You can't divide by 0")
finally:
	print('All Done')

print('\n## Problem 3')
def ask():
	while True:
		try:
			number = int(input('Input an integer: '))
		except:
			print('An error occurred! Please try again!')
			continue
		else:
			print('Thank you, your number squared is: {}'.format(number**2))
			break

ask()