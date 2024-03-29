#!/usr/bin/python3
"""7-model_state_fetch_all module
Lists all state objects from the usa database
new concepts ***
pool_pre_ping -> makes sure that the connection doesn't cut out
randomly
->>> sql alchemy stuff
create_engine -> makes an engine that runs a mysql server.
create_all -> makes tables in sqlalchemy when called
it makes all tables defined in METADATA
METADATA -> holds all data concerning tables
sessionmaker ->> creates a function that returns session
objects when called
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(State).order_by(State.id).all():
        print("{}: {}".format(data.id, data.name))
