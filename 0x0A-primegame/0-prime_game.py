#!/usr/bin/python3
"""Prime game"""


def isPrime(n):
    """Checks if a number is prime"""
    if n == 1:
        return False
    if n == 2:
        return True
    d = n // 2 + 1
    while d > 1:
        if n % d == 0:
            return False
        d = d - 1
    return True


def game_win(x, nums):
    """Returns win of round"""
    count = 0
    try:
        if x < 1 and len(nums) < 0:
            return None
        for i in range(x):
            if isPrime(nums[i]):
                count += 1
    except Exception:
        return None
    if count % 2 == 0 or x == 1:
        return "Ben"
    return "Maria"


def isWinner(x, nums):
    """Returns game winner"""
    Maria= 0
    Ben = 0
    win = None
    for i in range(x):
        n_list = []
        for num in range(nums[i] + 1):
            n_list.append(num + 1)
        win = game_win(nums[i], n_list)
        if win == "Ben":
            Ben += 1
        if win == "Maria":
            Maria += 1
    if Ben > Maria:
        return "Ben"
    if Maria > Ben:
        return "Maria"
    return None
