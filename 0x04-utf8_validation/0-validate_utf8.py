#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.

    Args:
        data(list): data set

    Returns:
        Boolean: True if data set represents a valid UTF-8 encoding else False
    """
    result = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:

        mask_byte = 1 << 7

        if result == 0:

            while mask_byte & byte:
                result += 1
                mask_byte = mask_byte >> 1

            if result == 0:
                continue

            if result == 1 or result > 4:
                return False

        else:
            if not (byte & mask_1 and not (byte & mask_2)):
                    return False

        result -= 1

    if result == 0:
        return True

    return False
