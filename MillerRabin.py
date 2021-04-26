# -*- coding: windows-1250 -*-
from secrets import randbelow
from ModPow import mod_pow
def miller_rabin(n, k):
    if n < 1 or n == 4:
        return False
    if n <= 3:
        return True
    m = n -1 
    while m % 2 == 0:
        m = int(m / 2)
    a = 0
    for _ in range(k):
        test = 0
        while a == 0 or a == 1:
            a = randbelow(n - 1)   
        x = mod_pow(a,m,n)
        if x == 1 or x == n - 1: 
            continue
        while m != n - 1:
            x = (x*x) % n
            m = m * 2
            if x == 1:
                return False
            if x == n-1:
                test = 1
                break
        if test == 1:
            continue
        return False
    return True