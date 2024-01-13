#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: nqueens N")

try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit("N must be a number")

if n < 4:
    sys.exit("N must be at least 4")


def queens(n, a=[], b=[], c=[]):
    """ Search for possible positions """
    if len(a) == n:
        yield a
    else:
        idx = len(a)
        for j in range(n):
            if j not in a and idx + j not in b and idx - j not in c:
                yield from queens(n, a + [j], b + [idx + j], c + [idx - j])


def solve(n):
    """ Queens solution """
    for solution in queens(n):
        print([list(enumerate(solution))])


if __name__ == "__main__":
    solve(n)
