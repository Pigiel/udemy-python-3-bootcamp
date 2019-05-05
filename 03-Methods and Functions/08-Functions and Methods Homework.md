# Functions and Methods Homework
Complete the following questions:

**Write a function that computes the volume of a sphere given its radius.**

The volume of a sphere is given as
> 4/3 πr^3

```py
def vol(rad):
	return (4/3) * (3.14) * (rad**3)
```
```sh
vol(2)
33.49333333333333
```
**Write a function that checks whether a number is in a given range (inclusive of high and low)**
```py
def ran_check(num,low,high):
	if num in range(low, high):
		return print(f'{num} is in range between {low} and {high}')
	else:
		return print('{} is in not range between {} and {}'.format(num, low, high))
```
```sh
ran_check(5,2,7)
5 is in the range between 2 and 7
```
If you only wanted to return a boolean:
```py
def ran_bool(num,low,high):
	return num in range(low, high)
```
```sh
ran_bool(3,1,10)
True
```
**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
```
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
```
HINT: Two string methods that might prove useful: `.isupper()` and `.islower()`

If you feel ambitious, explore the Collections module to solve this problem!
```py
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
```
```sh
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
No. of Upper case characters :  4
No. of Lower case Characters :  33
```
**Write a Python function that takes a list and returns a new list with unique elements of the first list.**
```
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
```
```py
def unique_list(lst):
	return print(list(set(lst)))
```
```sh
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
[1, 2, 3, 4, 5]
```
**Write a Python function to multiply all the numbers in a list.**
```
Sample List : [1, 2, 3, -4]
Expected Output : -24
```
```py
def multiply(numbers):
	result = numbers[0]
	for num in numbers:
		result *= num
	return result
```
```sh
multiply([1,2,3,-4])
-24
```
**Write a Python function that checks whether a passed in string is palindrome or not.**

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
```py
def palindrome(s):
	return s == s[::-1] 
```
```sh
palindrome('helleh')
True
```
### Hard:
**Write a Python function to check whether a string is pangram or not.**

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: Look at the string module

```py
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
	alphabet = set(alphabet)
	return alphabet <= set(str1.lower())
```
```sh
ispangram("The quick brown fox jumps over the lazy dog")
True
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
```
## Great Job!