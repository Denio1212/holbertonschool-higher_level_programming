#!/usr/bin/python3
"""
Takes the name of state as argument and lists all cities that match its id
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    inputs = argv[4]

    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8", port=3306) as db:
        cursor = db.cursor()
        executee = "SELECT *" \
                   "FROM cities" \
                   "JOIN states" \
                   " ON cities.state_id = states.id" \
                   " WHERE states.name=%s ORDER BY cities.id ASC"
        cursor.execute(executee, ('%' + inputs + '%',))
        content = cursor.fetchall()
        outcome = []
        for row in content:
            outcome.append(row[2])
            print(", ".join(outcome))
