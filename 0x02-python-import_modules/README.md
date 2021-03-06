# 0x02-python-import_modules

## Introduction to import and modules in Python

### 0-add.py
* Program that imports the function `def add(a, b):` from file `add_0.py` and prints `<a value> + <b value> = <add(a, b) value>` where
  * `a = 1`
  * `b = 2`
* Usage: `./0-add.py`
* Output: 
```
$ ./0-add.py
1 + 2 = 3
$
```

### 1-calculation.py
* Program imports the functions from `calculator_1.py` and does the calculations
  * `a = 10`
  * `b = 5`
* Usage: `./1-calculation.py`
* Output: \
```
$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
$
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
$
```

### 3-infinite_add.py
* Program adds all arguments
* Usage: `3-infinite_add.py`
* Sample output:\
```
$ ./3-infinite_add.py
0
$ ./3-infinite_add.py 79 10
89
$ ./3-infinite_add.py 79 10 -40 -300 89
-162
$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
$
```
### 4-hidden_discovery.py
* Program prints all names defined by compiled module `hidden_4.pyc`
* Usage: `./4-hidden_discovery.py`
* Output:
```
$ ./4-hidden_discovery.py
my_secret_santa
print_holberton
print_school
$
```

### 5-variable_load.py
* Program imports the variable `a` from file `variable_load_5.py` and prints its value
* Usage: `./5-variable_load.py`
* Sample output: /
```
$ ./5-variable_load.py
98
$
```

### 100-my_calculator.py
* Program imports functions from `calculator_1.py` and handles basic operations
  * addition (`+`)
  * subtraction (`-`)
  * multiplication (`*`)
  * division (`/`)
* Usage: `./100-my_calculator.py a operator b`
* Sample output:/
```
$ ./100-my_calculator.py
Usage: ./100-my_calculator.py <a> <operator> <b>
$ ./100-my_calculator.py 3 + 5
3 + 5 = 8
$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
$
```

### 101-easy_print.py
* Program prints `#pythoniscool`
* Usage: `./101-easy_print.py`
* Output:
```
$ ./101-easy_print.py
#pythoniscool
$
```

### 102-magic_calculation.py
* Python function that matches the given Python bytecode
```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

### 103-fast_alphabet.py
* Program prints the alphabet in uppercase
* Usage: `./103-fast_alphabet.py`
* Output:
```
$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
$
```
