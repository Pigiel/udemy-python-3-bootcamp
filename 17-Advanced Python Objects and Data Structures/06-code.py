#!/usr/bin/env python3

print('\n## Problem 1:')
print(bin(1024))
print(hex(1024))

print('\n## Problem 2:')
print(round(5.23222,2))

print('\n## Problem 3:')
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

print('\n## Problem 4:')
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

print('\n## Problem 5:')
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))

print('\n## Problem 6:')
print(set1.union(set2))

print('\n## Problem 7:')
print({x:x**3 for x in range(5)})

print('\n## Problem 8:')
list1 = [1,2,3,4]
list1.reverse()
print(list1)

print('\n## Problem 9:')
list2 = [3,4,2,5,1]
list2.sort()
print(list2)