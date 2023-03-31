#!/usr/bin/env python3
import subprocess
proc = subprocess.run(["ls", "-l"])
print(proc)
print(proc.returncode)
print(proc.args)
# no output stored so we have to pipe stderr and stdout to the variable
proc= subprocess.run(
    ["ls", "-l"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
print(proc.stdout)
print(proc.stdout.decode())
# working with stderr
proc = subprocess.run(["cat", "fake.txt"])
print(proc)
print(proc.returncode)
print(proc.args)
# working with stderr
proc = subprocess.run(["cat", "fake.txt"], check=True) # pass a flag to it
print(proc)
print(proc.returncode)
print(proc.args)