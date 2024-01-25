#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys

status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
size = 0
count = 0

try:
    for line in sys.stdin:
        lst = line.split(" ")
        if len(lst) > 4:
            code = lst[-2]
            size = int(lst[-1])
            if code in status_code.keys():
                status_code[code] += 1
            size += size
            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(size))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
