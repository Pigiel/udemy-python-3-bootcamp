#!/usr/bin/env python3
# Coding exercises for 09-Objects and Data Structures Assessment Test
###############################################################
print('\n## Numbers')
print('Equation: 60 + (10**2) / 4 * 5 - 84.75')
print(60 + (10**2) / 4 * 5 - 84.75)

print('What is the value of the expression 4 * (6 + 5)')
print(4 * (6 + 5))
print('What is the value of the expression 4 * 6 + 5 ')
print(4 * 6 + 5)
print('What is the value of the expression 4 + 6 * 5')
print(4 + 6 * 5 )
# Square root:
print('Square root: 100 ** 0.5')
print(100 ** 0.5)
# Square:
print('Square: 10 ** 2')
print(10 ** 2)
###############################################################
print('\n## Strings')
print("s = 'hello'")
s = 'hello'
# Print out 'e' using indexing
print('s[1] --> ' + s[1])
# Reverse the string using slicing
print('s[::-1] --> ' + s[::-1])
# Print out the 'o'
# Method 1:
print('s[-1] --> ' + s[-1])
# Method 2:
print('s[4] --> ' + s[4])
###############################################################
print('\n## Lists')
# Method 1:
print('[0]*3 --> ' + str([0]*3))
# Method 2:
print('list2 = [0,0,0]')
list2 = [0,0,0]
print('list2 --> ' + str(list2))

print("list3 = [1,2,[3,4,'hello']]")
list3 = [1,2,[3,4,'hello']]
print("list3[2][2] = 'goodbye'")
list3[2][2] = 'goodbye'
print('list3 --> ' + str(list3))

print('list4 = [5,3,4,6,1]')
list4 = [5,3,4,6,1]
# Method 1
print('sorted(list4) --> ' + str(sorted(list4)))
# Method 2
print('list4.sort()')
list4.sort()
print(list4)
###############################################################
print('\n## Dictionaries')
print("d = {'simple_key':'hello'}")
d = {'simple_key':'hello'}
# Grab 'hello'
print("d['simple_key'] --> " + str(d['simple_key']))

print("\nd = {'k1':{'k2':'hello'}}")
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print("d['k1']['k2'] --> " + str(d['k1']['k2']))

print("\nd = {'k1':[{'nest_key':['this is deep',['hello']]}]}")
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# Grab hello
print("d['k1'][0]['nest_key'][1][0] --> " + str(d['k1'][0]['nest_key'][1][0]))

# This will be hard and annoying!
print("\nd = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}")
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print("d['k1'][2]['k2'][1]['tough'][2][0] --> " + str(d['k1'][2]['k2'][1]['tough'][2][0]))
###############################################################
print('\n## Tuples')
t = (1,2,3)
print('t = (1,2,3) --> ' + str(t))
###############################################################
print('\n## Sets')
print('list5 = [1,2,2,33,4,4,11,22,3,3,2]')
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print('set(list5) --> ' + str(set(list5)))
###############################################################
print('\n## Booleans')
print('2 > 3 --> ' + str(2 > 3))
print('3 <= 2 --> ' + str(3 <= 2))
print('3 == 2.0 --> ' + str(3 == 2.0))
print('3.0 == 3 --> ' + str(3.0 == 3))
print('4**0.5 != 2 --> ' + str(4**0.5 != 2))

# two nested lists
print("l_one = [1,2,[3,4]]")
l_one = [1,2,[3,4]]
print("l_two = [1,2,{'k1':4}]")
l_two = [1,2,{'k1':4}]

# True or False?
print("l_one[2][0] >= l_two[2]['k1'] --> " + str(l_one[2][0] >= l_two[2]['k1']))