#!/usr/bin/python3
"""
Executes the previous code secure from injections
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    inputs = argv[4]

    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8", port=3306) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name\
         LIKE %s ORDER BY id ASC", ('%' + inputs + '%'))
        content = cursor.fetchall()
        for data in content:
            print(data)
