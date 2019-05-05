# Objects and Data Structures Assessment Test
## Test your knowledge.
### Answer the following questions

Write a brief description of all the following Object Types and Data Structures we've learned about:

**Numbers:** An object type represented by an integer (`int`) or floating point (`float`)

**Strings:** Any text information inside single (`' '`) or double quotes (`" "`) represented as character object type

**Lists:** An ordered object type constructed with square brackets `[]` and separated by commas that contain any object type (`string`, `int`, `float`). Lists are mutable

**Tuples:** An ordered object type constructed with brackets `()` and separated by commas that contain any object type (`string`, `int`, `float`). Tuples are immutable

**Dictionaries:** An unordered object type constructed with curly brackets `{}` having `'key':'value'` pair and separated by commas that contain any object type (`string`, `int`, `float`, `list`, other `dict`).

## Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
```py
60 + (10**2) / 4 * 5 - 84.75
```
```sh
100.25
```

Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)

What is the value of the expression 4 * 6 + 5 

What is the value of the expression 4 + 6 * 5 

```py
4 * (6 + 5)
```
```sh
44
```
```py
4 * 6 + 5
```
```sh
29
```
```py
4 + 6 * 5 
```
```sh
34
```
What is the type of the result of the expression `3 + 1.5 + 4`?
> Floating point number

What would you use to find a number’s square root, as well as its square?
```py
# Square root:
100 ** 0.5
```
```sh
10.0
```
```py
# Square:
10 ** 2
```
```sh
100
```

## Strings
Given the string `'hello'` give an index command that returns `'e'`. Enter your code in the cell below:
```py
s = 'hello'
# Print out 'e' using indexing
s[1]
```
```sh
'e'
```
Reverse the string `'hello'` using slicing:
```py
s ='hello'
# Reverse the string using slicing
s[::-1]
```
```sh
'olleh'
```
Given the string `'hello'`, give two methods of producing the letter `'o'` using indexing.
```py
s ='hello'
# Print out the 'o'
# Method 1:
s[-1]
```
```sh
'o'
```
```py
# Method 2:
s[4]
```
```sh
'o'
```

## Lists
Build this list `[0,0,0]` two separate ways.
```py
# Method 1:
[0]*3
```
```sh
[0, 0, 0]
```
```py
# Method 2:
list2 = [0,0,0]
list2
```
```sh
[0, 0, 0]
```
Reassign `'hello'` in this nested list to say `'goodbye'` instead:
```py
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
list3
```
```sh
[1, 2, [3, 4, 'goodbye']]
```
Sort the list below:
```py
list4 = [5,3,4,6,1]
# Method 1
sorted(list4)
```
```sh
[1, 3, 4, 5, 6]
```
```py
# Method 2
list4.sort()
list4
```
```sh
[1, 3, 4, 5, 6]
```

## Dictionaries
Using keys and indexing, grab the `'hello'` from the following dictionaries:
```py
d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']
```
```sh
'hello'
```
```py
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']
```
```sh
'hello'
```
```py
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# Grab hello
d['k1'][0]['nest_key'][1][0]
```
```sh
'hello'
```
```py
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]
```
```sh
'hello'
```
Can you sort a dictionary? Why or why not?
> No, because dictionaries are `key:value` mappins without any order


## Tuples
What is the major difference between tuples and lists?
> List are mutable and tuples are immutable

How do you create a tuple?
```py
t = (1,2,3)
```

## Sets
What is unique about a set?
> They don't allow to duplicate items

Use a set to find the unique values of the list below:
```py
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
```
```sh
{1, 2, 3, 4, 11, 22, 33}
```

## Booleans
For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

| Operator | Description | Example
| --- | --- | --- |
|==|If the values of two operands are equal, then the condition becomes true.|(a == b) is not true.|
|!=|If values of two operands are not equal, then condition becomes true.|(a != b) is true.|
|>|If the value of left operand is greater than the value of right operand, then condition becomes true.|(a > b) is not true.|
|<|If the value of left operand is less than the value of right operand, then condition becomes true.|(a < b) is true.|
|>=|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.|(a >= b) is not true.|
|<=|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|(a <= b) is true.|

What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
```py
 # Answer before running cell
2 > 3
```
```sh
False
```
```py
# Answer before running cell
3 <= 2
```
```sh
False
```
```py
# Answer before running cell
3 == 2.0
```
```sh
False
```
```py
# Answer before running cell
3.0 == 3
```
```sh
True
```
```py
# Answer before running cell
4**0.5 != 2
```
```sh
False
```
Final Question: What is the boolean output of the cell block below?
```py
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
```
```sh
False
```
## Great Job on your first assessment!