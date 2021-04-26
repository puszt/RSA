# -*- coding: windows-1250 -*-
def eucalg(a,b):
    if b!=0:
        return eucalg(b, a%b)
    return a