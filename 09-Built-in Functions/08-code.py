#!/usr/bin/env python3
###############################################################
print('\n## Problem 1')
def word_lengths(phrase):
	return list(map(len, phrase.split()))

print("word_lengths('How long are the words in this phrase')")
print(word_lengths('How long are the words in this phrase'))
###############################################################
print('\n## Problem 2')
from functools import reduce
def digits_to_num(digits):
	return reduce(lambda x,y: x*10 + y, digits)

print('digits_to_num([3,4,3,2,1])')
print(digits_to_num([3,4,3,2,1]))
###############################################################
print('\n## Problem 3')
def filter_words(word_list, letter):
	return filter(lambda word: word[0]==letter, word_list)

print("l = ['hello','are','cat','dog','ham','hi','go','to','heart']")
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print("filter_words(l,'h')")
print(list(filter_words(l,'h')))
###############################################################
print('\n## Problem 4')
def concatenate(L1, L2, connector):
	return list(word1 + connector + word2 for (word1, word2) in zip(L1, L2))

print("concatenate(['A','B'],['a','b'],'-')")
print(concatenate(['A','B'],['a','b'],'-'))
###############################################################
print('\n## Problem 5')
def d_list(L):
	return {key : value for value, key in enumerate(L)}

print("d_list(['a','b','c'])")
print(d_list(['a','b','c']))
###############################################################
print('\n## Problem 6')
def count_match_index(L):
	return len([num for count, num in enumerate(L) if num == count])

print('count_match_index([0,2,2,1,5,5,6,10])')
print(count_match_index([0,2,2,1,5,5,6,10]))