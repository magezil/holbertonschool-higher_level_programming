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
