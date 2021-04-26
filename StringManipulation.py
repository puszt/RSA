import time
import random
import string

def chunk_split(m,n):
    chunks = [m[i:i+n] for i in range(0, len(m), n)]
    return chunks

def converting_ints_withsplit(c = []):
    coded_string_message = []
    coded_string = ''.join(str(x) for x in c)
    coded_string_split = chunk_split(coded_string,3)
    for splitling in coded_string_split:
        coded_letter = chr(int(splitling))
        coded_string_message.append(coded_letter)
    coded_message = ''.join(coded_string_message)
    return coded_message

def converting_ints(c = []):
    decoded_message_letters = []
    for number in c:
        decoded_letter = chr(number)
        decoded_message_letters.append(decoded_letter)
    decoded_message = ''.join(decoded_message_letters)
    return decoded_message

def decoding_randchars (message):
    n = len(message)
    sub_message = ''
    k = 1
    for i in message:
        sub_message = sub_message + i
        for _ in range(30):  
            chars = string.ascii_letters + string.punctuation + string.digits
            b = sub_message+''.join(random.choice(chars) for _ in range(n-k))
            print (b, end="\r")
            time.sleep(.01)
        k = k + 1   
    input()