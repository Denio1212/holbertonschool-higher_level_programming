#!/usr/bin/python3
"""
    Selects all states from the USA database
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2], database=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states ORDER BY id ASC")
        table = db.fetchall()
        for data in table:
            print(data)
