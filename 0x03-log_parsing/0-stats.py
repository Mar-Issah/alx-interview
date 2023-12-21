#!/usr/bin/python3

import sys


def _print(status_code, file_size):
    """
    Method to print
    Args:
        status_code: status codes
        file_size: total size of the file

    Returns:
        None
    """

    print("File size: {}".format(file_size))

    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
code = 0
counter = 0


try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in status_code.keys()):
                    status_code[code] += 1

            if (counter == 10):
                _print(status_code, file_size)
                counter = 0

finally:
    _print(status_code, file_size)
