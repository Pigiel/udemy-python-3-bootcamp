# Iterators and Generators Homework
## Problem 1
Create a generator that generates the squares of numbers up to some number N.
```py
def gensquares(N):
	for x in range(N):
		yield x**2
```
```py
for x in gensquares(10):
    print(x)
```
```
0
1
4
9
16
25
36
49
64
81
```
## Problem 2
Create a generator that yields `"n"` random numbers between a low and high number (that are inputs). 
Note: Use the random library. For example:
```py
import random

random.randint(1,10)
```
```
9
```
```py
def rand_num(low,high,n):
	for x in range(n):
		yield random.randint(low, high)
```
```py
for num in rand_num(1,10,12):
    print(num)
```
```
6
1
10
5
8
2
8
5
4
5
1
4
```
## Problem 3
Use the `iter()` function to convert the string below into an iterator:

```py
s = 'hello'

#code here
s = iter(s)
print(next(s))
```
## Problem 4
Explain a use case for a generator using a `yield` statement where you would not want to use a normal function with a return statement.
> `yield` statement is more memory efficient for large iteration functions, because thay don't store output in memory  

## Extra Credit!
Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
```py
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
```
```
4
5
```
*Hint: Google generator comprehension!*

### Solution

A generator expression is like a list comprehension, but instead of finding all the items you're packing them into list, it waits, and yields each item out of the expression, one by one
```py
>>> my_list = [1, 3, 5, 9, 2, 6]
>>> filtered_list = [item for item in my_list if item > 3]
>>> print filtered_list
[5, 9, 6]
>>> len(filtered_list)
3
>>> # compare to generator expression
... 
>>> filtered_gen = (item for item in my_list if item > 3)
>>> print filtered_gen  # notice it's a generator object
<generator object at 0xb7d5e02c>
>>> len(filtered_gen) # So technically, it has no length
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'generator' has no len()
>>> # We extract each item out individually. We'll do it manually first.
... 
>>> filtered_gen.next()
5
>>> filtered_gen.next()
9
>>> filtered_gen.next()
6
>>> filtered_gen.next() # Should be all out of items and give an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> # Yup, the generator is spent. No values for you!
... 
>>> # Let's prove it gives the same results as our list comprehension
... 
>>> filtered_gen = (item for item in my_list if item > 3)
>>> gen_to_list = list(filtered_gen)
>>> print gen_to_list
[5, 9, 6]
>>> filtered_list == gen_to_list
True
>>> 
```

## Great Job!