# -*- coding: windows-1250 -*-
from secrets import randbits, randbelow
from MillerRabin import miller_rabin
from EuclideanAlgorithm import eucalg
from ModInverse import mod_inverse

def KeyGen():
    while True:
        p = randbits(10)
        q = randbits(10)
        if miller_rabin(p, 10) == True and miller_rabin(q, 10) == True:
            break
    n = p * q
    fi_n = (p - 1)*(q - 1)
    while True:
        e = 0
        while e == 0 or e == 1:
                e = randbelow(fi_n)
        if eucalg(e,fi_n) == 1:
            break
    d = mod_inverse(e, fi_n)

    return e,d,n,p,q
