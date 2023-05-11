#!/usr/bin/python3
"""11-model_state_insert module
Adds Louisiana as a state on the database
***
Session.add -> creates an object in the database
Session.Commit -> works the same way as with git commit
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="Louisiana"))
    session.commit()

    for data in session.query(State).filter_by(name="Louisiana"):
        print(data.id)
    session.close()
