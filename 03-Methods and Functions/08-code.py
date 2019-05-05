import string
###############################################################
print('\n## Volume of a shpere')

def vol(rad):
	return (4/3) * (3.14) * (rad**3)

print('vol(2)')
print(str(vol(2)))
###############################################################
print('\n## Number in range')

def ran_check(num,low,high):
	if num in range(low, high):
		return print(f'{num} is in range between {low} and {high}')
	else:
		return print('{} is in not range between {} and {}'.format(num, low, high))

print('ran_check(5,2,7)')
ran_check(5,2,7)

def ran_bool(num,low,high):
	return num in range(low, high)

print('ran_bool(3,1,10)')
print(str(ran_bool(3,1,10)))
###############################################################
print('\n## Upper/Lower letter counter')

def up_low(s):
	upper_letters, lower_letters = 0, 0
	for char in s:
		if char.isupper() == True:
			upper_letters += 1
		elif char.islower():
			lower_letters += 1
		else:
			pass

	print('Original string : ' + s)
	print(f'No. of Upper case characters: {upper_letters}')
	print(f'No. of Lower case characters: {lower_letters}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
###############################################################
print('\n## List of unique elements')

def unique_list(lst):
	return print(list(set(lst)))

print('unique_list([1,1,1,1,2,2,3,3,3,3,4,5])')
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
###############################################################
print('\n## Multiply all numbers in a list')

def multiply(numbers):
	result = numbers[0]
	for num in numbers:
		result *= num
	return result

print('multiply([1,2,3,-4])')
print(multiply([1,2,3,-4]))
###############################################################
print('\n## Palindrome')

def palindrome(s):
	return s == s[::-1]

print("palindrome('helleh')")
print(palindrome('helleh'))
###############################################################
print('\n## Pangram')

def ispangram(str1, alphabet=string.ascii_lowercase):
	alphabet = set(alphabet)
	return alphabet <= set(str1.lower())

print('ispangram("The quick brown fox jumps over the lazy dog")')
print(ispangram("The quick brown fox jumps over the lazy dog"))