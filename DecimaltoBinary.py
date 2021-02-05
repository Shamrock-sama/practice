# -*- coding:UTF-8 -*-
'''''
sub-function to convert decimal to binary
'''

import struct


def Int16(num):
    return bin(num).replace('0b', '').rjust(16, '0')[8:16] \
           + bin(num).replace('0b', '').rjust(16, '0')[0:8]


def Int32(num):
    return bin(num).replace('0b', '').rjust(32, '0')[24:32] \
           + " " + bin(num).replace('0b', '').rjust(32, '0')[16:24] \
           + " " + bin(num).replace('0b', '').rjust(32, '0')[8:16] \
           + " " + bin(num).replace('0b', '').rjust(32, '0')[0:8]

def Float32(num):
    return bin(sum(b << 8*i for i,b in enumerate(struct.pack('f', num)))).replace('0b', '').rjust(32, '0')[24:32] \
           + " " + bin(sum(b << 8*i for i,b in enumerate(struct.pack('f', num)))).replace('0b', '').rjust(32, '0')[16:24] \
           + " " + bin(sum(b << 8*i for i,b in enumerate(struct.pack('f', num)))).replace('0b', '').rjust(32, '0')[8:16] \
           + " " + bin(sum(b << 8*i for i,b in enumerate(struct.pack('f', num)))).replace('0b', '').rjust(32, '0')[0:8]


num = 42
if num < 0:
    num += 2**16
A = Int32(num)
print(A)

