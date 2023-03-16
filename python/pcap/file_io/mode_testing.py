#!/usr/bin/env python3
import os
import errno
import io
# mode      meaning                   file doesn't exist      existing data
# r         open for read             error                   n/a
# w         open for write            create one              truncate and start writing from 0th position
# a         open for append           create one              not removed
# r+        open for read and write   error                   not removed
# w+        open for write and read   create one              truncate and start writing from 0th position
# a+        open for append and read  create one              not removed
# x         open for creation
#
# t you will be a t back, b you will get bytes back

# if we open for read and it doesn't exist it will raise errno
# if we try to use read(file_handle) it will raise invalid as it knows
# that the file handle was obtained for write only


# todo
# add error checking with errno on file open
# change input to take filename in

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
    f = open(in_file, in_mode)
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