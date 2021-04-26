# -*- coding: windows-1250 -*-
def mod_inverse(a, m):
    m0 = m
    x = 1
    y = 0
    if m == 0:
        return 1
    while a > 1:
        q = a // m 
        b = m
        m = a % m 
        a = b 
        b = y 
        y = x - q * y 
        x = b 
    if x < 0:
        x = x + m0 
    return x