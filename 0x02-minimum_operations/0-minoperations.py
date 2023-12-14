#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """
    Gets fewest # of operations needed to result in exactly n H characters
    Args:
    n: The number of times
    Returns: operations

    """
    if (n < 2):
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1
    return operations
