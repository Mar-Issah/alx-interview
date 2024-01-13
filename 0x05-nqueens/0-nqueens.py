#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, idx=0, a=[], b=[], c=[]):
    """ Search for possible positions """
    if idx < n:
        for j in range(n):
            if j not in a and idx + j not in b and idx - j not in c:
                yield from queens(n, idx + 1, a + [j], b + [idx + j], c + [idx - j])
    else:
        yield a


def solve(n):
    """ Queens solution """
    k = []
    idx = 0
    for solution in queens(n, 0):
        for sol in solution:
            k.append([idx, sol])
            idx += 1
        print(k)
        k = []
        idx = 0


if __name__ == "__main__":
    solve(n)
