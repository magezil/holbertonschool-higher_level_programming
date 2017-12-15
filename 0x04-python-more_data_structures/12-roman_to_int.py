#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    letters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    last = len(roman_string) - 1
    skip = False
    result = 0
    for i in range(last, -1, -1):
        if i == 0 and skip is False:
            result += letters[roman_string[i]]
            break
        if skip:
            skip = False
            continue
        p = i - 1
        if letters[roman_string[p]] < letters[roman_string[i]]:
            diff = letters[roman_string[i]] - letters[roman_string[p]]
            result += diff
            skip = True
        else:
            result += letters[roman_string[i]]
    return result
#    if roman_string and type(roman_string) is str:
#        roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
#        value = 0
#        skip = False
#        for c, n in zip(roman_string, roman_string[1:]):
#            if roman_dict[c] < roman_dict[n]:
#                value -= roman_dict[c]
#            else:
#                value += roman_dict[c]
#        value += roman_dict[roman_string[-1]]
#        return value
#    else:
#        return 0
