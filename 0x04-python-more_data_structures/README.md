# 0x04-python-more_data_structures

## Python - More data structures: Set, Dictionary

### 0-square_matrix_simple.py
* Function computes the square value of all integers of a matrix
* Prototype: `def square_matrix_simple(matrix=[]):`
  * matrix: the matrix to use for computation
* Return: new matrix same size as `matrix` with each value squared
 
### 1-search_replace.py
* Function replaces all occurances of an element with another in a list
* Prototype: `def search_replace(my_list, search, replace):`
  * my_list: initial list
  * search: element to replace
  * replace: new element after replace
* Return: new list with replacement

### 2-uniq_add.py
* Function adds only the unique integers in a list
* Prototype: `def uniq_add(my_list=[]):`
  * my_list: initial list
* Return: sum of unique integers

### 3-common_elements.py
* Function returns a set of common elements in two sets
* Prototype: `def common_elements(set_1, set_2):`
  * set_1: first set
  * set2: second set
* Return: set of common elements of `set_1` and `set_2`

### 4-only_diff_elements.py
* Function returns a set of elements only in one set
* Prototype: `def only_diff_elements(set_1, set_2):`
  * set_1: first set
  * set2: second set
* Return: set of elements in only one set

### 5-number_keys.py
* Function returns number of keys in a dictionary
* Prototype: `def number_keys(my_dict):`
  * my_dict: dictionary to count keys
* Return: number of keys in `my_dict`

### 6-print_sorted_dictionary.py
* Function prints a dictionary of sorted keys
* Prototype: `def print_sorted_dictionary(my_dict):`
  * my_dict: dictionary to print sorted keys

### 7-update_dictionary.py
* Function replaces or adds a key:value to a dictionary
* Prototype: `def update_dictionary(my_dict, key, value):`
  * my_dict: dictionary to replace or add
  * key: key to replace or add
  * value: new value
* Return: updated dictionary

### 8-simple_delete.py
* Function deletes a key in dictionary
* Prototype: `def simple_delete(my_dict, key=""):`
  * my_dict: dictionary to delete key from
  * key: key to del
* Return: updated dictionary

### 9-multiply_by_2.py
* Function returns new dictionary with all values multiplied by 2
* Prototype: `def multiply_by_2(my_dict):`
  * my_dict: dictionary to operate on
* Return: new dictionary

### 10-best_score.py
* Function returns key with biggest integer value
* Prototype: `def best_score(my_dict):`
  * my_dict: dictionary to operate on
* Return: largest score, `None` if no score found

### 11-mutiply_list_map.py
* Function returns a list with all values multiplied by a number
* Prototype: `def mutiply_list_map(my_list=[], number=0):`
  * my_list: list of numbers
  * number: number to multiply by
* Return: new list with multiplied values

### 12-roman_to_int.py
* Function converts a Roman numeral into an integer
* Prototype: `def roman_to_int(roman_string):`
  * roman_string: Roman numeral to convert
* Return: integer value

### 100-weight_average.py
* Function returns the weighted average of a list of integer tuples
* Prototype: `def weight_average(my_list=[]):`
  * my_list: list of tuples `(<score>, <weight>)`
* Return: weighted average

### 101-square_matrix_map.py
* Function computes the square value of all integers of a matrix using `map`
* Prototype: `def square_matrix_map(matrix=[]):`
  * matrix: the matrix to use for computation
* Return: new matrix same size as `matrix` with each value squared

### 102-complex_delete.py
* C functions that print some basic info about Python lists and Python bytes objects
* Prototype: `void print_python_list(PyObject *p);`
* Prototype: `void print_python_bytes(PyObject *p);`
* Compile with `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
* Example:
```
$ cat 103-tests.py 
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["Holberton"]
lib.print_python_list(l)
lib.print_python_bytes(l);
$
$ python3 103-tests.py
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
```
