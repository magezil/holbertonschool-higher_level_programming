# 0x0D-SQL_introduction

## Introduction to SQL and databases
### 0-list_databases.sql
* Lists all databases in MySQL server

### 1-create_database_if_missing.sql
* Adds the database `hbtn_0c_0` to MySQL server

### 2-remove_database.sql
* Delete database `hbtn_0c_0` from server

### 3-list_tables.sql
* Show tables of a database in MySQL server

### 4-first_table.sql
* Create new table `first_table` in current database
  * `id`: INT
  * `name`: VARCHAR(256)

### 5-full_table.sql
* Prints full description of table `first_table` from the given database
  * Does not use `DESCRIBE` or `EXPLAIN`

### 6-list_values.sql
* Lists all rows of table `first_table` from given database

### 7-insert_value.sql
* Insert a new row into table `first_table`
  * `id=89`, `name='Holberton School'`

### 8-count_89.sql
* Count the number of records with `id=89` in table `first_table` of given database

### 9-full_creation.sql
* Create a new table `second_table` in given database and adds multiple rows
  * `id`: INT
  * `name`: VARCHAR(256)
  * `score`: INT
* Records to add:
  * id = 1, name = “John”, score = 10
  * id = 2, name = “Alex”, score = 3
  * id = 3, name = “Bob”, score = 14
  * id = 4, name = “George”, score = 8
### 10-top_score.sql
* Lists all records of `second_table`

