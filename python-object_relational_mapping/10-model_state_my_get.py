#!/usr/bin/python3
"""10-model_state_my_get module
The same as the previous but with changing arguments

nothing too special in this one
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(State).filter_by(name=argv[4]):
        print(data.id)
        exit()
    print("Not found")
    session.close()
