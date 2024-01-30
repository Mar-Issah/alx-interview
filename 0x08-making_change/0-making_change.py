#!/usr/bin/python3
""" Change comes from within"""


def makeChange(coins, total):
    """
    Function that returns the fewest number of coins needed to meet total
    Params:
        coins(list): list of coins
        total(int): total

    Returns: fewest number of coins needed to meet total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
