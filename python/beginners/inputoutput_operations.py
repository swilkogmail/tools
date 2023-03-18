#!/usr/bin/python3
# type casting - going from one datatype to another
print(float(1))
print(int(1.3))
print(int(1.8))
print(str(1.0))
# value error if you try to convert something that can't be converted
# print(int('1.2'))
# bool of any string or integer is true unless it is a null or zero
print(bool(1))
print(bool(0))
print(bool(1.7))
print(bool('hello'))
print(bool(''))

'''
when used with and it will return the first falsey value, i.e. this and that will return that this and 0 and that will return 0
'''
print('this' and 'that')
print('this' and 'that' and 1)
