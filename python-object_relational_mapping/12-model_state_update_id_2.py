#!/usr/bin/python3
"""12-model_state_update_id_2 module
Changes the name of state whose id is 2
***
Class.(attribute) -> can be used to change all sorts
of things
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all()

    Session = sessionmaker(bind=engine)
    session = Session()

    for mehico in session.query(State).filter_by(id=2):
        State.name = "New Mexico"
    session.commit()
    session.close()
