#!/usr/bin/python3
# the all means that if someone does "from helper import *" they will only get the ones in the list
# __all__ = ['extract_upper']
if __name__ == "__main__":
    print(f"Hello from helpers")
# returns only the uppercase characters
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

# returns only the lowercase characters
def extract_lower(phrase):
    return list(filter(str.islower, phrase))
