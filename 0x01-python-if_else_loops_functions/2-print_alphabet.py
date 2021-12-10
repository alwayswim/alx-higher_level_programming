#!/usr/bin/python3
alphabet = ""
for number in range(97, 123):
    alphabet = alphabet + chr(number)
    number += 1
print("{:s}".format(alphabet))
