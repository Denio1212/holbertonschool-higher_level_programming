#!/usr/bin/python3
"""
So we filter now. makes a script that lists all states with an
upper N
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], port=3306) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
        table = cursor.fetchall()
        for data in table:
            print(data)
