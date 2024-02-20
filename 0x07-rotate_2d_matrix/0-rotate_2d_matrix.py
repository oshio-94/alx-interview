#!/usr/bin/python3
"""
 Rotate a matrix
"""


def rotate_2d_matrix(matrix):
    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    L = len(matrix)
    for i in range(L//2):
        for j in range(L):
            matrix[j][i], matrix[j][L-1-i] = matrix[j][L-1-i], matrix[j][i]
    return matrix
