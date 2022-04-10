#!/usr/bin/python3
""" Contains `a`
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":

    ml = 'mysql+mysqldb://'
    lh = '@localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]

    engine = create_engine('{}{}:{}{}/{}'.format(ml, user, passwd, lh, db))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).\
        filter(State.name == arg)

    i = 0

    for state in result:
        print(state.id)
        i = 1
    if i != 1:
        print("Not found")
