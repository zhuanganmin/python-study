#!/usr/bin/python
#encoding: utf-8

from Crypto.Random import random
import binascii
from Crypto.Hash import SHA256
from Crypto.Cipher import AES



hash=SHA256.new()
hash.update('message'.encode('utf-8'))
print(hash.digest())

obj=AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message="The answer is no"
ciphertext=obj.encrypt(message)
print(ciphertext)
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
orgstr=obj2.decrypt(ciphertext)
print(orgstr)

random.choice(['dogs', 'cats', 'bears'])
