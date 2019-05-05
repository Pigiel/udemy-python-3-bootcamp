#!/usr/bin/env python3
###############################################################
print('\nPrint only the words that start with s in this sentence')
st = 'Print only the words that start with s in this sentence'
#Code here
for word in st.split():
	if word[0] == 's':
		print(word)
###############################################################
#Code Here
print('\nlist(range(0,11,2))')
print(list(range(0,11,2)))
###############################################################
#Code in this cell
print('\n[x for x in range(1,51) if x % 3 == 0]')
print([x for x in range(1,51) if x % 3 == 0])
###############################################################
print('\nPrint every word in this sentence that has an even number of letters')
st = 'Print every word in this sentence that has an even number of letters'
#Code in this cell
for word in st.split():
	if len(word) % 2 == 0:
		print(word)
###############################################################
#Code in this cell
for x in range(1,101):
	if x % 3 == 0 and x % 5 == 0:
		print('FizzBuzz')
	elif x % 3 == 0:
		print('Fizz')
	elif x % 5 == 0:
		print('Buzz')
	else:
		print(x)
###############################################################
print('\nCreate a list of the first letters of every word in this string')
st = 'Create a list of the first letters of every word in this string'
#Code in this cell
print('[word[0] for word in st.split()]')
print([word[0] for word in st.split()])