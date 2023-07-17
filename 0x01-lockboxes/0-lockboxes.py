#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    opened = [0]
    for idx, box in enumerate(boxes):
        # Empty list
        if not box:
            continue
        for key in box:
            if key != idx and key < len(boxes) and key not in opened:
                opened.append(key)
    if len(boxes) == len(opened):
        return True
    return False
