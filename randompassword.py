# -*- coding:UTF-8 -*-
'''
This project is aimed to generate a random password to secure your account
Author:Zhujin
'''

'''
8 characters password with:
2 uppercase letters from A to Z
2 lowercase letters from a to z
2 digits from 0 to 9
2 puncutation signs such as !, ?, ", # etc
'''

import random
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
digits1 = str(random.randint(0, 9))
digits2 = str(random.randint(0, 9))
punctuation1 = chr(random.randint(32, 47))
punctuation2 = chr(random.randint(32, 47))

password = [uppercase1, uppercase2, lowercase1, lowercase2, digits1, digits2, punctuation1, punctuation2]
print(uppercase1 + uppercase2 + lowercase1 + lowercase2 + digits1 + digits2 + punctuation1 + punctuation2)
password = shuffle(password)
print(password)