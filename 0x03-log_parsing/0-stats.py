#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys


def printstatus_code(lst, size):
    """ WWPrints information """
    print("File size: {:d}".format(size))
    for i in sorted(lst.keys()):
        if lst[i] != 0:
            print("{}: {:d}".format(i, lst[i]))


status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printstatus_code(status_code, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in status_code:
                status_code[stlist[-2]] += 1
        except:
            pass
    printstatus_code(status_code, size)


except KeyboardInterrupt:
    printstatus_code(status_code, size)
    raise
