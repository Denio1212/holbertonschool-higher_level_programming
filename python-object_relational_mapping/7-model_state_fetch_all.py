#!/usr/bin/python3
"""
Lists all state objects from the usa database
"""
from sqlalchemy import create_engine

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2],
                            argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(State).order_by(State.id).all():
        print("{}:{}".format(data.id, data.name))
    session.close()

