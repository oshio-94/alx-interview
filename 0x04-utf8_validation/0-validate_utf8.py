#!/usr/bin/python3
"""
This module contains a method that determines if a given data set
is valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given data set is valid UTF-8 encoding.
    """
    # number of bytes in the current UTF-8 character being processed
    number_of_bytes = 0
    mask = 255  # 11111111 in binary (8 bits)

    for value in data:
        # Check if the first bit is a 0
        if number_of_bytes == 0:
            # mask out the first bit
            value = value & mask
            # Check if the first 5 bits are 110 (0b110xxxxx)
            if (value >> 5) == 0b110:
                number_of_bytes = 1
            # Check if the first 4 bits are 1110 (0b1110xxxx)
            elif (value >> 4) == 0b1110:
                number_of_bytes = 2
            # Check if the first 3 bits are 11110 (0b11110xxx)
            elif (value >> 3) == 0b11110:
                number_of_bytes = 3
            # check if the first bit is a 1 (0b1xxxxxxx)
            elif (value >> 7):
                return False
        else:
            # Check if the first 2 bits are 10 (0b10xxxxxx)
            if (value >> 6) != 0b10:
                return False
            # Decrement the number of bytes in the current UTF-8 character
            number_of_bytes -= 1

    return number_of_bytes == 0
