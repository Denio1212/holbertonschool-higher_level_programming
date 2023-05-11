#!/usr/bin/python3
"""8-model_state_fetch_first module
a script that prints the first object from the database

first -> returns the first object in a sql query
under a given criteria
query -> it basically allows accessing and tinkering
the tables
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).first()
    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")
