#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string or type(roman_string) is str:
        roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        value = 0
        for c, n in zip(roman_string, roman_string[1:]):
            if roman_dict[c] < roman_dict[n]:
                value -= roman_dict[c]
            else:
                value += roman_dict[c]
        value += roman_dict[roman_string[-1]]
        return value
    else:
        return 0
