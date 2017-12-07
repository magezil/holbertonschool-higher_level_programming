# 0x02-python-import_modules

## Introduction to import and modules in Python

### 0-add.py
* Program that imports the function `def add(a, b):` from file `add_0.py` and prints `<a value> + <b value> = <add(a, b) value>` where
  * `a = 1`
  * `b = 2`
* Usage: `./0-add.py`
* Output: `1 + 2 = 3`

### 1-calculation.py
* Program imports the functions from `calculator_1.py` and does the calculations
  * `a = 10`
  * `b = 5`
* Usage: `./1-calculation.py`
* Output: \
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

### 2-args.py
* Program prints the number of and list of arguments
* Usage: `./2-args.py [args]`
* Sample output:\
```
$ ./2-args.py 
0 arguments.
$ ./2-args.py Hello
1 argument:
1: Hello
$ ./2-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
```
