#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise

    Args:
        matrix (list[[list]]): the matrix
    """
    num = len(matrix)
    for idx in range(int(num / 2)):
        y = (num - idx - 1)
        for j in range(idx, y):
            x = (num - 1 - j)
            tmp = matrix[idx][j]
            matrix[idx][j] = matrix[x][idx]
            matrix[x][idx] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
