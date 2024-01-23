def safe_print_division(a, b):
    result = None
    try:
        if a > b:
            result = a / b
        elif b > a:
            result = b / a
    except (ValueError, TypeError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(result), end="\n")

    return result
