#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Doc"""
    if n <= 0:
        return []

    triangle = []
    for i in range(0, n):
        x = 1
        num_list = []
        for k in range(0, i + 1):
            num_list.append(x)
            x = x * (i - k) // (k + 1)
        triangle.append(num_list)
    return(triangle)
