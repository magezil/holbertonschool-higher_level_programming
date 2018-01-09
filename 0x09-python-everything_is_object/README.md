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
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

### 9-answer.txt
* The following lines print `True` because `s1` and `s2` do point to the same object because `str`s are immutable. Python automatically creates an alias for immutable types with the same value.
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

### 10-answer.txt
* The following lines print `True` since the values of `l1` and `l2` are the same.
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

### 11-answer.txt
* The following lines print `False` because `l1` and `l2` are not aliases. Because lists are mutable, Python does not automatically create aliases for lists with the same value.
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

### 12-answer.txt
* The following code prints `True` because `l1` and `l2` refer to the same list and will have the same value
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

### 13-answer.txt
* The following lines print `True` because `l1` and `l2` are aliases.
```
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
* This script prints `[1, 2, 3, 4]` because `l1` and `l2` are aliases. Adding a value to one list adds it to the next one.
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
