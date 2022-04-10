#!/usr/bin/python3
""" Delete states
"""


from ast import keyword
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
    result = State.__table__.delete().\
        where(State.name.op('regexp')('a'.format(keyword)))
    session.execute(result)
    session.commit()
