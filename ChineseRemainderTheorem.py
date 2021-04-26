# -*- coding: windows-1250 -*-
from ModInverse import mod_inverse

def chinese_remainder_theorem(c = [], m = []):
    Mi = []
    M = 1
    yi = []
    for i in m:
        M = M*i
    x = 0
    for i in range(len(c)):
        Mi.append(M / m[i])
        yi.append(mod_inverse(Mi[i], m[i]))
        x = int(x) + int(c[i]) * int(Mi[i]) * int(yi[i])
    x = x % M 
    return x
