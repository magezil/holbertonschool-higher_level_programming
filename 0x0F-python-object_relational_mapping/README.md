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
* Script takes in arguments, sanitizes it, and siplay all states with matching name
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

