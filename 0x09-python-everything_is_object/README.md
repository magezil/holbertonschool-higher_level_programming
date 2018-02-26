# 0x09-python-everything_is_object
## Python - Everything is object

### 0-answer.txt
* Function used to print the type of an object

### 1-answer.txt
* Function to get the variable identifier

### 2-answer.txt
* In the following code `a` and `b` do not point to the same object since they are different values.
```python
>>> a = 89
>>> b = 100
```

### 3-answer.txt
* In the following code `a` and `b` do point to the same object because `int`s are immutable. Python automatically creates an alias for immutable types with the same value.
```python
>>> a = 89
>>> b = 89
```

### 4-answer.txt
* In the following code `a` and `b` do point to the same object because `b` is made an alias for `a`.
```python
>>> a = 89
>>> b = a
```

### 5-answer.txt
* In the following code `a` and `b` do not point to the same object because they have different values.
```python
>>> a = 89
>>> b = a + 1
```

### 6-answer.txt
* The following lines print `True` since the value of `s1` and `s2` are the same
```python
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

### 7-answer.txt
* The following lines print `True` because `s2` is made an alias of `s1`
```python
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

### 8-answer.txt
* The following lines print `True` since the value of `s1` and `s2` are the same
```python
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

### 9-answer.txt
* The following lines print `True` because `s1` and `s2` do point to the same object because `str`s are immutable. Python automatically creates an alias for immutable types with the same value.
```python
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

### 10-answer.txt
* The following lines print `True` since the values of `l1` and `l2` are the same.
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

### 11-answer.txt
* The following lines print `False` because `l1` and `l2` are not aliases. Because lists are mutable, Python does not automatically create aliases for lists with the same value.
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

### 12-answer.txt
* The following code prints `True` because `l1` and `l2` refer to the same list and will have the same value
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

### 13-answer.txt
* The following lines print `True` because `l1` and `l2` are aliases.
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

### 14-answer.txt
* This script prints `[1, 2, 3, 4]` because `l1` and `l2` are aliases. Appending a value to one list adds it to the next one.
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

### 15-answer.txt
* This script prints `[1, 2, 3]` because adding a value to a list in this way creates a new list. This means that `l1` and `l2` are no longer aliases
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

### 16-answer.txt
* This prints `1` because `int`s are immutable, so a new `int` object was created in the function and nothing changes what object `a` is referencing.
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

### 17-answer.txt
* This prints `[1, 2, 3, 4]` because the reference to `l` is passed into the function. Thus, when n is changed, l is also changed
```python
l = [1, 2, 3]
increment(l)
print(l)
```

### 18-answer.txt
* This prints `[1, 2, 3]` the function does not change the object that `l1` is referring to
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

### 19-copy_list.py
* Function that returns a copy of a list `l`
* Prototype: `def copy_list(l):`

## The questions 20-23 answer whether the given code is a tuple or not
### 20-answer.txt
* Yes, it is an empty tuple
```python
a = ()
```

### 21-answer.txt
* Yes, it is a tuple with 2 elements
```python
a = (1, 2)
```

### 22-answer.txt
* No, it is not enough to surround an item with parentheses to make a tuple. type(a) is an int
```python
a = (1)
```

### 23-answer.txt
* Yes, it is a tuple with 1 element
```python
a = (1, )
```
### 24-answer.txt
* `True` because two `int`s with the same value have the same id (are aliases)
```python
a = (1)
b = (1)
a is b
```

### 25-answer.txt
* `False` because each tuple will have its own id (they are not aliases) even if they have the same value. This is because the value of a tuple may change based on the object(s) references stored within it. For example, a tuple may hold references to `str`s or `list`s, which are mutable.
```python
a = (1, 2)
b = (1, 2)
a is b
```

### 26-answer.txt
* `True` since tuples are immutable so no value can be added to the empty tuple, both variables will reference the same empty tuple
```python
a = ()
b = ()
a is b
```

### 27-answer.txt
* The id of `a` will change because adding this way with lists creates a new id
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

### 28-answer.txt
* The id of `a` will not change because lists are mutable. As such, changing the list will not change the id
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

### 103-line1.txt, 103-line2.txt
* These files list how many int objects are created by each line of the following script
```python
a = 1
b = 1
```

### 104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt
```python
a = 1024
b = 1024
del a
del b
c = 1024
```
