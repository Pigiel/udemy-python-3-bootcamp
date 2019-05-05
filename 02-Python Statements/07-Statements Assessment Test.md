# Statements Assessment Test
Let's test your knowledge!

Use `for`, `.split()`, and `if` to create a Statement that will print out words that start with `'s'`:
```py
st = 'Print only the words that start with s in this sentence'
#Code here
for word in st.split():
	if word[0] == 's':
		print(word)
```
```
start
s
sentence
```
Use `range()` to print all the even numbers from 0 to 10.
```py
#Code Here
list(range(0,11,2))
```
```
[0, 2, 4, 6, 8, 10]
```
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
```py
#Code in this cell
[x for x in range(1,51) if x % 3 == 0]
```
```sh
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
```
Go through the string below and if the length of a word is even print "even!"
```py
st = 'Print every word in this sentence that has an even number of letters'
#Code in this cell
for word in st.split():
	if len(word) % 2 == 0:
		print(word)
```
```
word
in
this
sentence
that
an
even
number
of
```
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
```py
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
```
Use List Comprehension to create a list of the first letters of every word in the string below:
```py
st = 'Create a list of the first letters of every word in this string'
#Code in this cell
[word[0] for word in st.split()]
```
```sh
['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
```
## Great Job!