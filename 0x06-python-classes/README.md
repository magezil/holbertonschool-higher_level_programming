# 0x06-python-classes

## Python - Classes and Objects
### 0-square.py
* Empty class `Square`

### 1-square.py
* Class `Square` with private instance attribute `size`

### 2-square.py
* Class `Square` with validated private instance attribute `size`

### 3-square.py
* Class `Square` with validated private instance attribute `size`
* Instance method `area` - returns area of current `Square` instance
  * Prototype: `def area(self):`

### 4-square.py
* Class `Square` with validated private instance attribute `size`
  * Property `size` now included to set and get `size`
* Instance method `area` - returns area of current `Square` instance
  * Prototype: `def area(self):`

### 5-square.py
* Class `Square` with validated private instance attribute `size`
  * Property `size` to set and get `size`
* Instance method `area` - returns area of current `Square` instance
  * Prototype: `def area(self):`
* Instance method `my_print` - prints to stdout the square with `#` or empty line if size == 0
  * Prototype: `def my_print(self):`

### 6-square.py
* Class `Square` with validated private instance attributes `size` and `position`
  * Property `size` to set and get `size`
  * Property `position` to set and get `position`
* Instance method `area` - returns area of current `Square` instance
  * Prototype: `def area(self):`
* Instance method `my_print` - prints to stdout the square with `#` or empty line if size == 0
  * Prototype: `def my_print(self):`

### 100-singly_linked_list.py
* Class `Node` that is a node of a singly linked list
* Instantiate: `def __init__(self, data, next_node=None):`
* Private instance attribute `data`
  * property `def data(self):` to retrieve
  * property setter `def data(self, value)` to set
* Private instance attribute `next_node`:
  * property `def next_node(self):` to retrieve
  * property setter `def next_node(self, value):` to set

* Class `SinglyLinkedList` is a singly linked list and is printable
* Instantiate: `def __init__(self):`
* Private instance attribute `head`
* Public instance method `def sorted_insert(self, value):`
  * Add new `Node` to correct sorted position (increasing order)

### 101-square.py
* Make printing `Square` instance have same behavior as `my_print()`, based on `6-square.py`

### 102-square.py
* Add comparison functionality to `Square` class based on `4-square.py`

### 103-magic_class.py
* `MagicClass` that matches the Python bytecode
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
