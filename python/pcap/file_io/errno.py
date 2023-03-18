#!/usr/bin/python3
import errno
import os

try:
    f = open('fask.txt','r')
except OSError as err:
    if err.errno == errno.ENOENT:
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")
    elif err.errno == errno.EACCES:
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")
# FileNotFoundError: [Errno 2] No such file or directory: 'fask.txt'
# man errno and grep for No such file or directory
# ENOENT 2 No such file or directory
# https://docs.python.org/3/library/errno.html
# the dictionary that maps from errors to names:


