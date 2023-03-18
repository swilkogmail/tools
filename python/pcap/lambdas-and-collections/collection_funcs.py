#!/usr/bin/python3
# higher order fuctions can take a function as an argument or it will return a function
from functools import reduce
domain = [1,2,3,4,5]


# f(x) = x * 2

# map takes two arg, function name (which can be a lambda, and a domain)
# takes a collection as input and doubles its vales and returns a list the same size
our_range = map(lambda num: num * 2, domain)
# needs tobe coverted to a list otherwise returns a map object
# range and domain always the same size
print(list(our_range))

# result you get is alwas the same length as the domain that is supplied

evens = filter(lambda num: num % 2 == 0, domain)
# everything in python returns a true or false,
print(list(evens))

# pulled in from functools
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
# acc = accumlator.  It takes 0 to initiate the number, loops through the domain list and sums each of the output
print(the_sum)


words = ['Boss', 'a', 'Alfred', 'Fig', 'Daemon', 'dig']
print("sorting by default")
print(sorted(words))

# before the sort is performed we modify the orginal item to lower case and then sorted based on this
print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))

# str.lower("my_string") is the same as "my_string".lower()

# lists are mutable so they can be changes
print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)


words = ['Boss', 'a', 'Alfred', 'Fig', 'Daemon', 'dig', '10', '5']
print("sorting by default")
print(sorted(words))
