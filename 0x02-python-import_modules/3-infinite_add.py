#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numargs = len(argv) - 1
    ans = 0
    for i in range(1, numargs + 1):
        ans += int(argv[i])
    print("{:d}".format(ans))
