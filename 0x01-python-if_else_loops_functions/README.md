# 0x01-python-if_else_loops_functions

## Introduction to if, else, loops, and functions in Python

### 0-positive_or_negative.py
* Python script that prints whether a random number `number` is positive or negative
* Usage: `./0-positive_or_negative.py`

### 1-last_digit.py
* Python script prints the last digit of a random number `number` and whether the digit is:
  * greater than 5
  * less than 6 and not 0
  * 0
* Usage: `./1-last_digit.py`

### 2-print_alphabet.py
* Python script prints the alphabet in lower case
* Usage: `./2-print_alphabet.py`
* Output:\
`abcdefghijklmnopqrstuvwxyz$`

### 3-print_alphabt.py
* Python script that prints the alphabet in lower case except for `e` and `q`
* Usage: `./3-print_alphabt.py`
* Output:\
`abcdfghijklmnoprstuvwxyz$`

### 4-print_hexa.py
* Python script that prints numbers `0` to `98` in decimal and hexidecimal
* Usage: `./4-print_hexa.py`
* Output:\
```
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
$
```

### 5-print_comb2.py
* Python script prints numbers `00` to `99` separated by a `, `
* Usage: `./5-print_comb2.py`
* Output:\
```
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
$
```

### 6-print_comb3.py
* Python script prints all possible combinations of two unique digits
  * `01` and `10` are considered the same
* Usage: `./6-print_comb3.py`
* Output:\
```
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
$
```

### 7-islower.py
* Python function checks for a lower case character
* Prototype: `def islower(c):`
* Return: `True` if c is lowercase, `False` otherwise
