#!/usr/bin/python3
# Consider the code snippet below:

from random import sample
 
list_1 = [x << 1 for x in range(1,12,3)]
# range(1,12,3) is a sequence that includes numbers from 1 (included) to 12 (not included) with a step of 3 - in other words :
[1, 4, 7, 10]
# Operator << is a bitwise operator ("left shift"). x << 1 is equivalent to 2 * x.
# So:  [x << 1 for x in range(1,12,3)] (a list comprehension) will return the following list:

# so list_1 = [2, 8, 14, 20]

list_2 = sample(list_1, 3)
# sample() is a function from the random module that returns a list of k items chosen randomly from a sequence. 
# Its syntax is : sample(sequence, k) where:
# sequence : can be a list, tuple, string or set.
# k: integer value that specifies the number of elements to pick

# so list_2 = sample([2, 8, 14, 20], 3)

# will return a list of 3 elements chosen randomly from [2, 8, 14, 20]; 
# this could be : [2, 14, 20]  or [2, 8, 20]  or [8, 14, 20]  etc ...

list_3 = list(filter(lambda x: x > 3, list_2))
# Finally this will produce a list out of list_2 where each element x of list_2 that cannot satisfy x > 3 is discarded.
# Based on this rule, there are not a lot of possible outcomes : this could be : [14, 20]  or [8, 14]  or [8, 20]  or [8, 14, 20]
# (note : order may change - i.e. [14, 20] or [20, 14] are possible outcomes).

print(list_3)

# left shift mutiples by 2
list_1 = [x for x in range(1,12,3)] # 2 * x
print(list_1)
list_1 = [x << 1 for x in range(1,12,3)] # 2 * x
print(list_1)
list_1 = [x << 2 for x in range(1,12,3)] # 4 * x
print(list_1)
list_1 = [x << 3 for x in range(1,12,3)] # 8 * x
print(list_1)
list_1 = [x << 4 for x in range(1,12,3)] # 16 * x
print(list_1)


# right shift divides by 2 and dicards the remainder
list_1 = [x for x in range(1,12,3)] # 2 / x
print(list_1)
list_1 = [x >> 1 for x in range(1,12,3)] # 2 / x
print(list_1)
list_1 = [x >> 2 for x in range(1,12,3)] # 4 / x
print(list_1)
list_1 = [x >> 3 for x in range(1,12,3)] # 8 / x
print(list_1)
list_1 = [x >> 4 for x in range(1,12,3)] # 16 * x
print(list_1)