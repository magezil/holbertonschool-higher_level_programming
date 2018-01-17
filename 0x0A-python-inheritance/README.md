# 0x0A-python-inheritance

## Python - Inheritance
### 0-lookup.py
* Function returns list of available attributes and methods of an object 
* Prototype: `def lookup(obj):`

### 1-my_list.py  
* Creates a class MyList that inherits from list
* Public instance method: `def print_sorted(self):`
  * Function prints list in ascending sorted order

### 2-is_same_class.py  
* Function that checks if an object is an instance of the specified class
* Prototype: `def is_same_class(obj, a_class):`
* Return: `True` if it is, `False` otherwise

### 3-is_kind_of_class.py  
* Function that checks if an object is an instance of the specified class or class that inherited from specified class
* Prototype: `def is_kind_of_class(obj, a_class):`
* Return: `True` if it is, `False` otherwise

### 4-inherits_from.py  
* Function checks if an object is an instance of a class that inherited (directly or indirectly) from specified class

### 5-base_geometry.py  
* Create empty class `BaseGeometry`

### 6-base_geometry.py  
* Class `BaseGeometry`
* Public instance method: `def area(self):`
  * Raise Exception("area() is not implemented")

### 7-base_geometry.py  
* Class `BaseGeometry` with new functionality
* Public instance method: `def integer_validator(self, name, value):`
  * name: string name of variable to validate
  * value: value to validate if positive int

### 8-rectangle.py  
* Class `Rectangle` inherits `BaseGeometry`
* Instantiate private instance fields `width` and `height` validated with `integer_validator()`

### 9-rectangle.py  
* Class `Rectangle` inherits from `BaseGeometry` with additional functionality
* implement `area()` method
* implement `print()` and `__str__()` to print and return, respectively, `[Rectangle] <width>/<height>`

### 10-square.py  
* Class `Square` inherits from `Rectangle`
* Instantiate private instance field `size`
* Implement `area()`

### 11-square.py  
* Class `Square` inherits from `Rectangle` with additional functionality
* implement `print()` and `__str__()` to print and return, respectively, `[Square] <width>/<height>`

### 100-my_int.py  
* Class `MyInt` inherits from `int`
* Implement functionality of rebel child
  * invert `==` and `!=` operators

### 101-add_attribute.py  
* Function adds attribute to class if possible
* Prototype: `def add_attribute(obj, attribute, value):`
