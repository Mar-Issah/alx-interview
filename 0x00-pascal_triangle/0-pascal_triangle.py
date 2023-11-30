#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """function def pascal_triangle(n)

    Returns: a list of lists
    Returns: an empty list if n <= 0

    """
    result = []
    if n > 0:
        for idx in range(1, n + 1):
            row = []
            C = 1
            for j in range(1, idx + 1):
                row.append(C)
                C = C * (idx - j) // j
            result.append(row)
    return result
