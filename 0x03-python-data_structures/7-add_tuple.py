#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tupl = ()
    tuple_alen = len(tuple_a)
    tuple_blen = len(tuple_b)
    count = 0
    if (tuple_alen == tuple_blen):
        while count < tuple_alen:
            tupl += (tuple_a[count] + tuple_b[count],)
            count = count + 1
    elif tuple_alen > tuple_blen:
        while count < tuple_alen:
            if count >= tuple_blen:
                tupl += (tuple_a[count],)
            else:
                tupl += (tuple_a[count] + tuple_b[count],)
            count = count + 1
    elif tuple_blen > tuple_alen:
        while count < tuple_blen:
            if count >= tuple_alen:
                tupl += (tuple_b[count],)
            else:
                tupl += (tuple_a[count] + tuple_b[count],)
            count = count + 1
    return tupl
