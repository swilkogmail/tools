#!/usr/bin/python3
# What do you need to replace zzz with to get the following printed to the monitor: (1, 1, 27) ?
# correct answer:
# mylist2 = tuple(filter(lambda x: x % 2 != 0, mylist1))
#
# 1. (1, 1, 27) is a tuple
mylist1 = [x**x for x in range(4)]
# note - range starts with so x is 0,1,2,3
# 0**0 = 1 anything to the power 0 is 1
for x in range(4):
    print(str(x)+" power "+ str(x) +" = " + str(x**x))
# my list is built by 0..3 being raised by the power of itself
print(mylist1)
# lambda x: x % 2 != 0, mylist1
# take mylist as an input to the lambda function, i.e. [1, 1, 4, 27] and discard the even numbers, i.e. x % 2 != 0
# filter(lambda x: x % 2 != 0, mylist1) filters mylist1 whilst using the first argument lambda x: x % 2 != 0 to test which ones to keep (just the odd ones)
mylist2 = tuple(filter(lambda x: x % 2 != 0, mylist1))
print(mylist2)
# map(lambda x: x % 2 != 0, mylist1) would return True, True, False, True - the results of the function but not filtered
mylist3 = tuple(map(lambda x: x % 2 != 0, mylist1))
print(mylist3)
# cast the result to a tuple to get (1, 1, 27)
# print(mylist2)