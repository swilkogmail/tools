#!/usr/bin/python3

# returns only the uppercase characters
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

# returns only the lowercase characters
def extract_lower(phrase):
    return list(filter(str.islower, phrase))
