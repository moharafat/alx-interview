#!/usr/bin/python3
""" determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """ valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        # Mask to get the last 8 bits of the integer
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if bin_rep.startswith('110'):
                n_bytes = 1
            elif bin_rep.startswith('1110'):
                n_bytes = 2
            elif bin_rep.startswith('11110'):
                n_bytes = 3
            elif bin_rep.startswith('10'):
                return False
        else:
            # Check if the next byte starts with '10'
            if not bin_rep.startswith('10'):
                return False
            n_bytes -= 1

    # If n_bytes is not zero, then we were expecting
    # more bytes to complete a character
    return n_bytes == 0
