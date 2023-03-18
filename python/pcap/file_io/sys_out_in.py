#!/usr/bin/python3
import sys
# stdin are readable and out and err is writable
sys.stdout.write("Testing\n")
sys.stderr.write("TestingErr\n")
# not recommended to close
lines = sys.stdin.readlines()
# this will hand and ctrl^D needed to break and write back to the variable
print(lines)