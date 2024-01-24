#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for loop in range(1, 3):

        try:
            if loop > a:
                raise Exception('Too far')
            else:
                result += a ** b / loop
        except Exception:
            result = a + b
            break
    return result
