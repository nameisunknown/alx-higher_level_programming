#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))

    except (TypeError, ValueError) as errmsg:
        sys.stderr.write("Exception: {}\n".format(errmsg))
        return False

    return True
