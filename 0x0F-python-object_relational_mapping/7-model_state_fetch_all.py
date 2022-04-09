#!/usr/bin/python3
""" All states via SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":

    ml = 'mysql+mysqldb://'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('{}{}:{}@localhost/{}'.format(ml, user, passwd, db))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))
