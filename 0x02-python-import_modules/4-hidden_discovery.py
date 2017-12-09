#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for d in dir():
        if d[0:2] != "__":
            print("{}".format(d))
