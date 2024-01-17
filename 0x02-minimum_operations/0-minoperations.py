#!/usr/bin/python3
"""
This module contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    write a method that calculates
    the fewest number of operations needed to result in exactly n H characters
    in the file
    """
    if n <= 1:
        return 0
    minnum, rem, numOfOperations = n, 2, 0
    while minnum > 1:
        if minnum % rem == 0:
            minnum = minnum / rem
            numOfOperations = numOfOperations + rem
        else:
            rem += 1
    return numOfOperations
