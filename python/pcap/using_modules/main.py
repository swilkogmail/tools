#!/usr/bin/python3
# import helpers # whole module
# from helpers import extract_lower, extract_upper # just the funcs you need
# from helpers import * # no need to prefix it with the module name (collisions more likely)
# print("importing helpers from main")
# modules will only be read in once
# from python.pcap.helpers.strings import extract_lower, extract_upper # aliasing the funcs if you have a variable assignment collision
from helpers.strings import extract_lower
from helpers import variables
# extract_upper will come from the import statement below
from helpers import *
import helpers

print(f"Lowercase Letters: {extract_lower(variables.name)}")
print(f"Lowercase Letters: {extract_upper(variables.name)}")
print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")