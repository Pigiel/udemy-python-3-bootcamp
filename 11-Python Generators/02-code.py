#!/usr/bin/env python3

print('\n## Problem 1\n')

def gensquares(N):
	for x in range(N):
		yield x**2

for x in gensquares(10):
	print(x)

print('\n## Problem 2\n')

import random

def rand_num(low,high,n):
	for x in range(n):
		yield random.randint(low, high)

for num in rand_num(1,10,12):
	print(num)

print('\n## Problem 3\n')

s = 'hello'

#code here
s = iter(s)
print(next(s))

print('\n## Extra Credit!\n')

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
	print(item)