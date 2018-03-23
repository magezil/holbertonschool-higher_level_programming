# 0x0F-python-object_relational_mapping

## Object-relational mapping - linking Python and Databases
### 0-select_states.py
* Script lists all `states` from database `hbtn_0e_0_usa`
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)

### 1-filter_states.py
* Script lists all `states` with a `name` starting with `N` from database `hbtn_0e_0_usa`
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)

### 2-my_filter_states.py
* Script takes in an argument and displays all values in `states` table that match argument
* Takes four arguments:
  * mysql username
  * mysql password
  * database name
  * state name to search
* Connects to default host (localhost) and port (3306)

### 3-my_safe_filter_states.py
* Script takes in arguments, sanitizes it, and display all states with matching name
* Takes four arguments:
  * mysql username
  * mysql password
  * database name
  * state name to search (to be sanitized) 
* Connects to default host (localhost) and port (3306)

### 4-cities_by_state.py
* Script lists all cities from database
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)

### 5-filter_cities.py
* Script takes state name as an argument and lists all cities of given state
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)

### model_state.py
* File contains class `State` and instance `Base = declarative_base()`
* `State` class:
  * inherits from `Base`
  * links to MySQL table `states`
  * class attributes:
    * `id` - represents a column of auto-generated, unique integer, can't be NULL, and is primary key
    * `name` - represents a column of string with max 128 characters, can't be NULL

### 7-model_state_fetch_all.py
* Script lists all State objects from given database
Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)

### 8-model_state_fetch_first.py
* Script prints first `State` object from database
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)
* Print `Nothing` if table is empty

### 9-model_state_filter_a.py
* Script lists all `State` objects that contain the letter `a`
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)
* Print `Nothing` if table is empty

### 10-model_state_my_get.py
* Script prints State object with the name passed as argument
* Takes three arguments:
  * mysql username
  * mysql password
  * database name
* Connects to default host (localhost) and port (3306)
* Print `Not found` if not found

