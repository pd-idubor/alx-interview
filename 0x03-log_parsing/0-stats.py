#!/usr/bin/python3
"""Log Parsing"""
import sys


def log_parser():
    """Log parser function"""
    codes = {"200": 0, "301": 0, "400": 0,
             "401": 0, "403": 0, "404": 0,
             "405": 0, "500": 0}
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            row = line.split()

            if len(row) >= 2 and len(row) <= 9:
                if row[-1].isdigit():
                    file_size += int(row[-1])
                if row[-2] in codes:
                    codes[row[-2]] += 1

            if line_count == 10:
                printer(codes, file_size)
        printer(codes, file_size)

    except KeyboardInterrupt:
        printer(codes, file_size)
        raise


def printer(codes, file_size):
    """Prints status codes and count"""
    print("File size: {}".format(file_size))
    for key in sorted(codes):
        if codes[key] != 0:
            print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    log_parser()
