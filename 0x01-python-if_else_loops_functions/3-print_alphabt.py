#!/usr/bin/python3
alphabet = ""
for number in range(97, 123):
    alphabet = alphabet + chr(number)
    number += 1
for elm in alphabet:
    if elm != "e" and elm != "q":
        print("{}".format(elm), end="")
