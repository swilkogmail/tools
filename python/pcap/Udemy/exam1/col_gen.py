#!/usr/bin/python3
import sys
in_col_list = ["File Status", "REALM", 10, "TABLE_NAME", 20, "FILE_ID", 30, "STATUS", 40, "SHIP_DURATION", 50, "APPLY_DURATION", 60]

# in_col_list = ["r", "REALM", 10, "TABLE_NAME", 20]

len_list = len(in_col_list)
row_type = in_col_list[0]
col_names = in_col_list[1::2]
col_lens = in_col_list[2::2]


def row_out(in_col_names, in_col_lens):
    num_cols = len(in_col_names)
    lp = 0
    for i in range(0,num_cols): # if n = 3 it will loop through twice
        column_heading = in_col_names[lp]
        column_length = in_col_lens[lp]
        pad = (column_length-1)
        heading = column_heading.ljust(pad," ")
        yield heading # 1st time return 1, 2nd time return  1(res) x 2
        lp+= 1


# it will always return the same as the range function always loops twice n to n+2 (increment by one)

if row_type == "r":
    title = row_type + " Detail:"
    print(title)
    print("")
else:
    heading_list = [row for row in row_out(col_names, col_lens)]
    heading = ''.join(heading_list)
    print(heading)