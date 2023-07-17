#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Doc"""
    if n <= 1:
        return 0

    i = 2
    min_op = 0

    while i <= n:
        if n % i == 0:
            min_op += i
            n /= i
        else:
            i += 1

    return min_op
