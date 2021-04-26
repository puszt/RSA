# -*- coding: windows-1250 -*-
def mod_pow(a, e, m):
    result = 1
    apow = a
    while e != 0 : 
        if (e & 0x01) == 0x01:
            result = (result * apow) % m 
        e >>= 1
        apow = (apow * apow) % m 
    return result
