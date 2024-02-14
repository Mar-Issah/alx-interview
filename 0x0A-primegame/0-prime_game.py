#!/usr/bin/python3
"""0. Prime Game """


def isWinner(x, nums):
    """
    Prime game
    Param:
    x(int) - the number of rounds
    nums(list) - lis of n

    Return: name of the player that won the most rounds

    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for idx in range(2, len(a)):
        remove_multiples(a, idx)

    for idx in nums:
        if sum(a[0:idx + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def remove_multiples(ls, x):
    """method to removes multiple primes
    """
    for idx in range(2, len(ls)):
        try:
            ls[idx * x] = 0
        except (ValueError, IndexError):
            break
