#!/usr/bin/python3
"""N Queens"""
import sys


def nPos(pos, row, i):
    """Checks for a position not within the queesn's spectrum"""
    for j in range(row):
        if(pos[j] == i or pos[j] + row - j == i or pos[j] + j - row == i):
            return False
    return True


def safePos(pos, row):
    """Check for next safe position"""
    for i in range(len(pos)):
        if nPos(pos, row, i):
            pos[row] = i
            if row < len(pos) - 1:
                safePos(pos, row + 1)
            else:
                print([[i, pos[i]] for i in range(len(pos))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])

except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
pos = [-1 for i in range(n)]
safePos(pos, 0)
