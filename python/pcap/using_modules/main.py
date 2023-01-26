#!/usr/bin/python3
# import helpers # whole module
# from helpers import extract_lower, extract_upper # just the funcs you need
# from helpers import * # no need to prefix it with the module name (collisions more likely)
# print("importing helpers from main")
# modules will only be read in once
from helpers import extract_lower, extract_upper # aliasing the funcs if you have a variable assignment collision
import extras

print(f"Lowercase Letters: {extract_lower(extras.name)}")
print(f"Lowercase Letters: {extract_upper(extras.name)}")