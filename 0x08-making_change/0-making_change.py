#!/usr/bin/python3
"""given a pile of coins of different values determine the fewest coins"""


def makeChange(coins, total):
    """determine the fewest number of coins"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, num_coins = (0, 0)
    total_coins = total
    denum = len(coins)

    while(i < denum and total_coins > 0):
        if (total_coins - coins[i]) >= 0:
            total_coins -= coins[i]
            num_coins += 1
        else:
            i += 1

    check = total_coins > 0 and num_coins > 0
    return -1 if check or num_coins == 0 else num_coins
