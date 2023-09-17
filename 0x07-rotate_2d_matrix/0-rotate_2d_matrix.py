#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate an n x n 2D matrix 90 degrees clockwise"""
    start = 0
    row_n = len(matrix) - 1
    while start < row_n:
        for x in range(start, row_n):
            tmp = matrix[x][row_n]
            matrix[x][row_n] = matrix[start][x]
            tmp1 = matrix[row_n][row_n + start - x]
            matrix[row_n][row_n + start - x] = tmp
            tmp = matrix[row_n + start - x][start]
            matrix[row_n + start - x][start] = tmp1
            matrix[start][x] = tmp
        start += 1
        row_n -= 1
