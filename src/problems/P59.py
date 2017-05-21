#!/usr/bin/env python3
"""P59 - XOR Decryption"""

from sys import argv
from string import ascii_lowercase
from itertools import product

WORDS = [[ord(c) for c in word] for word in [
    " the ", " and ", " that ", " have "]]

LETTERS = [ord(l) for l in ascii_lowercase]
PASSWORD_LENGTH = 3


def cyclic_iter(iterable, length):
    for _ in range(length):
        for item in iterable:
            yield item


def possible_passwords():
    return product(*(LETTERS for _ in range(PASSWORD_LENGTH)))


def decrypt(message, password):
    return [msg_char ^ pswd_char
            for msg_char, pswd_char in zip(
                message, cyclic_iter(password, len(message)))]


def guess_decryption(message):
    for password in possible_passwords():
        decrypted_msg = decrypt(message, password)
        if contains_any(decrypted_msg, WORDS):
            return decrypted_msg
    raise Exception("Couldn't decrypt message")


def contains_any(message, words):
    for word in words:
        for i in range(len(message) - len(word)):
            if message[i:i + len(word)] == word:
                return True
    return False


def main(filename):
    try:
        f = open(filename)
    except IOError:
        print("Error, could not open specified file.")
    else:
        with f:
            encrypted_msg = [int(c) for c in f.read().split(',')]
        msg = guess_decryption(encrypted_msg)
        return sum(msg)


if __name__ == '__main__':
    try:
        print(main(argv[1]))
    except IndexError:
        print("Error, specify file name.")

