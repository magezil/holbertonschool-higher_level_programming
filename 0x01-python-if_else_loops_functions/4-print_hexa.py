#!/usr/bin/python3
for i in range(99):
    print("{:d} = 0x".format(i), end="")
    if i // 16 >= 1:
        print(i // 16, end="")
        i %= 16
    if i >= 10 and i <= 15:
        print("abcdef"[i % 10])
    else:
        print(i % 16)
