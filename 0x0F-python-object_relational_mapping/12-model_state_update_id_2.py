#!/usr/bin/python3
""" Update a state
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

    engine = create_engine('{}{}:{}{}/{}'.format(ml, user, passwd, lh, db))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.id == 2).one()
    result.name = "New Mexico"
    session.commit()
