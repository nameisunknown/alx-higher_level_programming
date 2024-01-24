#!/usr/bin/python3

def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return result
