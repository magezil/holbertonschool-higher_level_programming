# 0x03-python-data_structures

## Python Data Structures: Lists, Tuples

### 0-print_list_integer.py
* Function prints all the integers in a list
* Prototype: `def print_list_integer(my_list=[]):`

### 1-element_at.py
* Function retrieves an element from a list (like C)
* Prototype: `def element_at(my_list, idx):`
* Return: specified element or `None` if `idx` is invalid

### 2-replace_in_list.py
* Function replaces an element at a specific position (like C)
* Prototype: `def replace_in_list(my_list, idx, element):`
* Return: list with specified element changed, or original list if `idx` is invalid


### 3-print_reversed_list_integer.py
* Function prints all integers in a list in reverse order
* Prototype: `3-print_reversed_list_integer.py`

### 4-new_in_list.py
* Function copies an element at a specific position without modifying the original list (like C)
* Prototype: `def new_in_list(my_list, idx, element):`
* Return: copy of list with specified element changed, or copy of original list if `idx` is invalid

### 5-no_c.py
* Function removes all `C` and `c` characters from a string
* Prototype: `def no_c(my_string):`
* Return: string without `C` or `c`

### 6-print_matrix_integer.py
* Function prints an integer matrix
* Prototype: `def print_matrix_integer(matrix=[[]]):` 

### 7-add_tuple.py
* Function adds two tuples
* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Return: tuple of (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])

### 8-multiple_returns.py
* Function returns tuple of string (length, first character)
* Prototype: `def multiple_returns(sentence):`
* Return: tuple of string (length, first character)

### 9-max_integer.py
* Function finds the largest number in a list
* Prototype: `def max_integer(my_list=[]):`
* Return: `None` if list is empty, largest number otherwise

### 10-divisible_by_2.py
* Function finds all multiples of 2 in a list
* Prototype: `def divisible_by_2(my_list=[]):`
* Return: list of `True` or `False` whether element at same position in `my_list` is a multiple of 2

### 11-delete_at.py
* Function deletes item at specified index
* Prototype: `def delete_at(my_list=[], idx=0):`
* Return: changed list 

### 12-switch.py
* Python script switches the values of `a` and `b`
* Usage: `./12-switch.py`

### 13-is_palindrome.c, lists.h
* C function that checks if a singly linked list is a palindrome
* Prototype: `int is_palindrome(listint_t **head);`
* Return: `0` if it is not a palindrome, `1` if it is

### 100-print_python_list_info.c
* C function that prints some basic information about Python lists
* Prototype: `void print_python_list_info(PyObject *p);`
* Print format:
```
[*] Size of the Python List = <size>
[*] Allocated = <space allocated>
Element 0: <type>
Element 1: <type>
...
Element <size - 1>: <type>
```
