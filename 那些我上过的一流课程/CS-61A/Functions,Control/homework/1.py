def a_plus_abs_b(a, b):
    """"
    Return a+abs(b), but without calling abs.
    """
    if b < 0:
        f = a-b
    else:
        f = a+b
    return f
    