# -*- coding: windows-1250 -*-
from ModInverse import mod_inverse
c = []
m = []
Mi = []
def chinese_remainder_theorem(c, m):
    M = 1
    yi = []
    for i in m:
        M = M*i
    x = 0
    for i in range(len(c)):
        Mi.append(M / m[i])
        print(Mi)
        yi.append(mod_inverse(Mi[i], m[i]))
        print(yi)
        x = x + c[i] * Mi[i] * yi[i]
    x = x % M 
    return x