#!/usr/bin/python3
import sys
import random

# this code is superceeded by the code below
# if len(sys.argv) < 2:
#     raise Exception('not enought arguments')

# name = sys.argv[1]
# print(f"Name is {name}")

# try:
#     print(f"First argument {sys.argv[1]}")
#     args = sys.argv
#     random.shuffle(args)
#     print(f"Random arguments {args[0]}")
# except (IndexError, KeyError) as err: # tuple can be used
#     print(f"Error: no arguments provided, please provide at least one ({err})")
# except NameError:
#     print(f"Error: random module not loaded")
# else:
#     print("else is running")
# finally:
#     print("finally is running")

from cli import main
from cli.errors import ArgumentError

# try:
#     main()
# except ArgumentError as err:
#     print(f"Error: {err}")
#     sys.exit(1)

# and using assertions
try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f"Error: {err}")
    sys.exit(1)

# problems with assert statements are they can be run in prodcution with
# -O which means they remove all assert statments
# -OO which means remove docstrings as well