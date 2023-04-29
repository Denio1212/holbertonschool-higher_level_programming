#!/usr/bin/python3
"""
Listing the cities in the database through ORM
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    with MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8") as db:
        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name"
                       "FROM cities "
                       "JOIN states "
                       "ON cities.state_id = states.id "
                       "ORDER BY cities.id ASC")
        content = cursor.fetchall()
        for data in content:
            print(data)
