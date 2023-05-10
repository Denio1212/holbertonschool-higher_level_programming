#!/usr/bin/python3
"""9-model_state_filter_a module
lists all objects containing a in the dbase
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(State).filter(State.name.like("%a%")). \
            order_by(State.id).all():
        print("{}: {}".format(data.id, data.name))
