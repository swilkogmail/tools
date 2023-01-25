#!/usr/bin/python3
# import helpers # whole module
# from helpers import extract_lower, extract_upper # just the funcs you need
# from helpers import * # no need to prefix it with the module name (collisions more likely)
from helpers import extract_lower as e_low, extract_upper # aliasing the funcs if you have a variable assignment collision

name = "Steve Wilkins"
print(f"Lowercase Letters: {e_low.extract_lower(name)}")
print(f"Lowercase Letters: {helpers.extract_upper(name)}")