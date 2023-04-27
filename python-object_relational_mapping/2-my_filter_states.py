#!/usr/bin/python3
"""
 Returns all states matchiing the argument
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    inputs = argv[4]

    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], port=3306) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name\
         LIKE '%{}%' ORDER BY id ASC".format(inputs))
        table = cursor.fetchall()
        for data in table:
            print(data)
