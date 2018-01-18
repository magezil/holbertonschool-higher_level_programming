# 0x0B-python-input_output

## Python - Input/Output
### 0-read_file.py  
* Function reads a text file in `UTF8` encoding and prints it to stdout
* Prototype: `def read_file(filename=""):`

### 1-number_of_lines.py  
* Function counts the number of lines in a text file
* Prototype: `def number_of_lines(filename=""):`
* Return: number of lines in text file

### 2-read_lines.py  
* Function reads `n` lines of a text file in `UTF8` encoding and prints it to stdout
* Prototype: `def read_lines(filename="", nb_lines=0):`

### 3-write_file.py  
* Function writes a string to a text file in `UTF8` encoding
* Prototype: `def write_file(filename="", text=""):`
* Return: number of characters written

### 4-append_write.py  
* Function appends a string to the end of a text file in `UTF8` encoding
* Prototype: `def append_write(filename="", text=""):`
* Return: number of characters added

### 5-to_json_string.py  
* Functioin returns JSON representation of a string object 
* Prototype: `def to_json_string(my_obj):`
* Return: JSON representation of object

### 6-from_json_string.py  
* Function returns object represented by JSON string
* Prototype: `def from_json_string(my_str):`
* Return: object

### 7-save_to_json_file.py  
* Function writes an Object to a text file using a JSON representation
* Prototype: `def save_to_json_file(my_obj, filename):`

### 8-load_from_json_file.py  
* Function creates an Object from a JSON file
* Prototype: `def load_from_json_file(filename):`
* Return: created object

### 9-add_item.py  
* Script adds all command line arguments to a Python list, save to a file
* Use functions from `7-save_to_json_file.py` and `8-load_from_json_file.py`
* Save to json file `add_item.json`

### 10-class_to_json.py  
* Function returns the dictionary description of simple data structure (list, dictionary, string, integer, boolean)
* Prototype: `def class_to_json(obj):`
* Return: dictionary of data structure

### 11-student.py  
* Class `Student`
* Public instance attributes: `first_name`, `last_name`, `age`
* Public method: `def to_json(self):`
  * Retrieves dictionary representation of `Student` instance

### 12-student.py  
* Class `Student`
* Public method: `def to_json(self, attrs=None):`
  * Retrieves dictionary representation of `Student` instance
  * If `attrs` is list of strings, return only attribute names in `attrs`
  * Else, return all attributes

### 13-student.py  
* Class `Student`
* Public method: `def reload_from_json(self, json):`
  * Replace all attributes of `Student` instance
  * Assume json will always be a dictionary
    * key: public attribute name
    * value: value of attribute

### 14-pascal_triangle.py  
* Function returns list of lists of integers representing Pascal's triangle of `n`
* Prototype: `def pascal_triangle(n):`
* Return: list of lists of Pascal's triangle
