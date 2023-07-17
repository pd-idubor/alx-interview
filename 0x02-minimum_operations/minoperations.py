#!/usr/bin/python3


def minOperations(n):
    if n <= 1:
        return 0

    i = 2
    min_o = 0
    m = 1
    while i <= n:
        if n % i == 0:
            n /= i
            min_o += i
        else:
            i += 1

    return min_o
