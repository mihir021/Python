def fac(n:int) -> int:
    p = 1
    while n > 0:
        p *= n
        n -= 1
    return p