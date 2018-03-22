#!/usr/bin/python3
"""Script takes in an argument and displays all values in states table that match argument
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name = %s\
            ORDER BY states.id ASC""", (argv[4], ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
