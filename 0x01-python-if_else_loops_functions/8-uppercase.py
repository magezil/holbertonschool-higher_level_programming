#!/usr/bin/python3
def uppercase(str):
    toup = ord('a') - ord('A')
    for c in str:
        print(chr(ord(c) - toup) if islower(c) else c, end="")
    print()


def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')
