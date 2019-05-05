#!/usr/bin/env python3
# Coding exercises for 03-Function-Practice-Exercises
###############################################################
print('\nLESSER OF TWO EVENS')

def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a,b)

print('lesser_of_two_evens(2,4) --> ' + str(lesser_of_two_evens(2,4)))
print('lesser_of_two_evens(2,5) --> ' + str(lesser_of_two_evens(2,5)))
###############################################################
print('\nANIMAL CRACKERS')

def animal_crackers(text):
	animals = text.split()
	return animals[0][0] == animals[1][0]

print("animal_crackers('Levelheaded Llama') --> " + str(animal_crackers('Levelheaded Llama')))
print("animal_crackers('Crazy Kangaroo') --> " + str(animal_crackers('Crazy Kangaroo')))
###############################################################
print('\nMAKES TWENTY')

def makes_twenty(n1,n2):
	return n1 == 20 or n2 == 20 or n1 + n2 == 20

print('makes_twenty(20,10) --> ' + str(makes_twenty(20,10)))
print('makes_twenty(12,8) --> ' + str(makes_twenty(12,8)))
print('makes_twenty(2,3) --> ' + str(makes_twenty(2,3)))
###############################################################
print('\nOLD MACDONALD')

def old_macdonald(name):
	if len(name) > 3:
		return name[:3].capitalize() + name[3:].capitalize()
	else:
		return 'Name is too short!'

print("old_macdonald('macdonald') --> " + old_macdonald('macdonald'))
###############################################################
print('\nMASTER YODA')

def master_yoda(text):
	return ' '.join(text.split()[::-1])

print("master_yoda('I am home') --> " + master_yoda('I am home'))
print("master_yoda('We are ready') --> " + master_yoda('We are ready'))
###############################################################
print('\nALMOST THERE')

def almost_there(n):
	return (abs(n-100) <= 10) or (abs(n-200) <= 10)

print('almost_there(90) --> ' + str(almost_there(90)))
print('almost_there(104) --> ' + str(almost_there(104)))
print('almost_there(150) --> ' + str(almost_there(150)))
print('almost_there(209) --> ' + str(almost_there(209)))
###############################################################
print('\nFIND 33')

def has_33(nums):
	for i in range(0, len(nums)-1):
		if nums[i] == 3 and nums[i+1] == 3:
			return True
	return False

print('has_33([1, 3, 3]) --> ' + str(has_33([1, 3, 3])))
print('has_33([1, 3, 1, 3]) --> ' + str(has_33([1, 3, 1, 3])))
print('has_33([3, 1, 3]) --> ' + str(has_33([3, 1, 3])))
###############################################################
print('\nPAPER DOLL')

def paper_doll(text):
	result = ''
	for char in text:
		result += char * 3
	return result

print("paper_doll('Hello') --> " + paper_doll('Hello'))
print("paper_doll('Mississippi') --> " + str(paper_doll('Mississippi')))
###############################################################
print('\nBLACKJACK')

def blackjack(a,b,c):
	if sum((a,b,c)) <= 21:
		return sum((a,b,c))
	elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
		return sum((a,b,c)) - 10
	else:
		return 'BUST'

print('blackjack(5,6,7) --> ' + str(blackjack(5,6,7)))
print('blackjack(9,9,9) --> ' + str(blackjack(9,9,9)))
print('blackjack(9,9,11) --> ' + str(blackjack(9,9,11)))
###############################################################
print("\nSUMMER OF '69")

def summer_69(arr):
	result = 0
	add = True
	for x in arr:
		while add:
			if x != 6:
				result += x
				break
			else:
				add = False
		while not add:
			if x != 9:
				break
			else:
				add = True
### Alternative solution
#	for x in arr:
#		if x == 6:
#			add = False
#		elif x == 9:
#			add = True
#		else:
#			if add == True:
#				result += x
	return result

print('summer_69([1, 3, 5]) --> ' + str(summer_69([1, 3, 5])))
print('summer_69([4, 5, 6, 7, 8, 9]) --> ' + str(summer_69([4, 5, 6, 7, 8, 9])))
print('summer_69([2, 1, 6, 9, 11]) --> ' + str(summer_69([2, 1, 6, 9, 11])))
###############################################################
print('\nSPY GAME')

def spy_game(nums):
	code = [0, 0, 7, 'x']

	for x in nums:
		if x == code[0]:
			code.pop(0)

	return len(code) == 1

print('spy_game([1,2,4,0,0,7,5]) --> ' + str(spy_game([1,2,4,0,0,7,5])))
print('spy_game([1,0,2,4,0,5,7]) --> ' + str(spy_game([1,0,2,4,0,5,7])))
print('spy_game([1,7,2,0,4,5,0]) --> ' + str(spy_game([1,7,2,0,4,5,0])))
###############################################################
print('\nCOUNT PRIMES')

def count_primes(num):
	primes = [2]
	x = 3
	
	if num < 2:
		return 0
	while x <= num:
		for y in range(3,x,2):
			if x%y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2
	
	print(primes)
	
	return len(primes)

print('count_primes(100)')
print(count_primes(100))
###############################################################
print('\nPRINT BIG')

def print_big(letter):
	patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
	alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
	for pattern in alphabet[letter.upper()]:
		print(patterns[pattern])

print("print_big('a')")
print_big('a')