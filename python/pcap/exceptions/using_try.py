#!/usr/bin/python3
import sys
import random

try:
    print(f"First argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random arguments {args[0]}")
except (IndexError, KeyError) as err: # tuple can be used
    print(f"Error: no arguments provided, please provide at least one ({err})")
except NameError:
    print(f"Error: random module not loaded")
else:
    print("else is running")
finally:
    print("finally is running")


## exceptions available
err = Exception('Something went wrong')
print(str(err))
print(dir(err))