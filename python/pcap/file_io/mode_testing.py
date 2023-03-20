#!/usr/bin/env python3
import os, errno, sys
# x - write only. EEXIST if file is already there
# r - read only. ENONENT is file does not exist.
# r+ - read and write. ENONENT is file does not exist.
# w - write only. Create file if not in existence
# w+ - write and read. Create file if not in existence
# a - append only.  Create file if not in existence
# a+ - append and read.  Create file if not in existence

mode = input("enter the mode that you want to test: ")
file = input("enter the name of the file: ")

def main():
    
    print(f"Opening {file} in {mode} mode...\n")
    f = open_file(file, mode)
    
    try:
        print(f"Writing data...\n")
        write_data(f)
    except:
        print(f"ERROR! {file} can't be written to!")
    else:
        print(f"Data written without problem...\n")
    
    try:
        print(f"Reading data...\n")
        contents = read_file(f)
    except:
        print(f"ERROR! {file} can't be read!")
    else:
        print(f"Data read without problem...\n")
    finally:
        close_file(f)
        print(f"{file} closed!\n\n")
        f = open_file(file, 'r')
        contents = read_file(f)
        print(f"The contents of file is now:\n{contents}")
        close_file(f)


def open_file(in_file, in_mode):
    f = ''
    try:
        f = open(in_file, in_mode)
    except OSError as err:
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}\n")
        print(f"file opened with {mode}")
        sys.exit(99)
    return f

def write_data(in_f):
    in_f.write(f"This is your file written by {__name__}\n")
    in_f.write('line 2\n')
    in_f.writelines([
        'line 3\n',
        'line 4\n',
        'line 5\n'])

def close_file(in_f):
    in_f.close()


def read_file(in_f):
    contents = ''
    try:
        in_f.seek(0)
        contents = in_f.read() # key error as not opened in read mode
    except OSError as err:
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")
    return contents

def remove_file(in_file):
    os.system(f"rm {in_file}")

main()