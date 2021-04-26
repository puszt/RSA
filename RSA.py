# -*- coding: windows-1250 -*-
from ModPow import mod_pow
from ChineseRemainderTheorem import chinese_remainder_theorem
from StringManipulation import converting_ints, converting_ints_withsplit,\
    decoding_randchars
from KeyGen import KeyGen


def RSA(message):
    # -*- Making ints of the message  
    message_letters = []
    coded_message_ints = []
    decoded_message_ints = []
    # -*- Appending the letters to the list
    for letter in message:
        message_letters.append(letter)
    # -*- generating the 'd' key, with p and q random primes, n as their product, and e
    e,d,n,p,q = KeyGen()
    # -*- Encryption 
    for letter in message_letters:
        # -*- converting ASCII to int
        m = ord(letter)
        # -*- calculating the 'c' components
        c = mod_pow(m, e, n)
        # -*- appending every c to a container
        coded_message_ints.append(c)
    # -*- this is only for optics
    coded_message = converting_ints_withsplit(coded_message_ints)
    print('Your coded message: ',coded_message,'\n')
    input('Press Enter to decode the coded message...')
    # -*- Decryption
    for c in coded_message_ints:
        # -*- reducing c
        reducedc1 = c % p 
        reducedc2 = c % q
        # -*- reducing d 
        reducedd1 = d % (p - 1)
        reducedd2 = d % (q - 1)
        # -*- congruence system 
        rsac = []
        rsam = []
        # -*- filling the c[] for chinese_remainder_theorem
        rsac.append(mod_pow(reducedc1, reducedd1, p))
        rsac.append(mod_pow(reducedc2, reducedd2, q))
        # -*- filling the m[] for chinese_remainder_theorem
        rsam.append(p)
        rsam.append(q)
        # -*- executing the chinese remainder theorem for every coded int, to get the original int
        message_int = chinese_remainder_theorem(rsac,rsam)
        decoded_message_ints.append(message_int)
    # -*- converting the ints back to ascii
    decoded_message = converting_ints(decoded_message_ints)
    print('\nYour original message: ')
    decoding_randchars(decoded_message)
