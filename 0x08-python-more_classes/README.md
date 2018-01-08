# 0x08-python-more_classes

## More Classes and Objects
### 0-rectangle.py
* Create an empty `Rectangle` class

### 1-rectangle.py
* Class `Rectangle`
* Private instance attribute `width`
  * Property to set and get
  * Raises:
    * TypeError: if `width` is not an integer
    * ValueError: if `width` is negative
* Private instance attribute `height`
  * Property to set and get
  * Raises:
    * TypeError: if `height` is not an integer
    * ValueError: if `height` is negative
* Instantiate: `def __init__(self, width=0, height=0):`

### 2-rectangle.py
* Add public instance methods `area` and `parameter`
* `def area(self):` - returns the rectangle area
* `def perimeter(self):` - returns the rectangle perimeter
  * if either `width` or `height` is `0` - return `0`

### 3-rectangle.py
* Adds functionality for print() and str()
  * should return an empty string if `width` or `height` are 0

### 4-rectangle.py
* Define `__repr__` to be able to create new instance of Rectangle

### 5-rectangle.py
* Print "Bye rectangle..." when instance is deleted

### 6-rectangle.py
* Add public class attribute `number_of_instances`
  * Number of instances of Rectangle
### 7-rectangle.py
### 8-rectangle.py
### 9-rectangle.py

### 101-nqueens.py
