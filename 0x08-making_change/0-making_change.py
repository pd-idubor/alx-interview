#!/usr/bin/python3
"""Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
    to meet a given amount total"""
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    num = 0
    for coin in coins:
        if coin <= total:
            num += total // coin
            total %= coin
            if total == 0:
                return num

    return -1
